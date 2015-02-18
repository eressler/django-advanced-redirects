import logging
import re

from django import http
from django.conf import settings
from django.utils.timezone import now

from .models import Redirect, Referral
from . import settings as redirect_settings

logger = logging.getLogger(__name__)


class AdvancedRedirectMiddleware(object):
    """
    This middleware checks to see if the current request has resulted in a 404 error, and if it has
    it then checks to see if there is a redirect specified.  If there is none, it will store the url that
    generated the 404 error.

    The middleware takes the full path of the request and attempts to find an existing redirect with and without
    an ending slash.  In this way, these two urls would be treated as the same URL instead of two different URLs:
    /dir/foo/bar/
    /dir/foo/bar
    """
    def get_response_class(self, redirect):
        """
        Utility function for determining which response class to use based on the redirect_type value.
        :return: Class
        """
        if redirect.redirect_type == redirect_settings.PERMANENT_REDIRECT_VALUE:
            return http.HttpResponsePermanentRedirect
        if redirect.redirect_type == redirect_settings.TEMPORARY_REDIRECT_VALUE:
            return http.HttpResponseRedirect

        raise NotImplementedError("The 'redirect_type' has not been implemented correctly. "
                                  "The values are specified in advanced_redirects.settings")

    def match_pattern(self, full_path, pattern, placeholder, field):
        redirect = None

        match = re.match(pattern, full_path)
        if match:
            group = match.groupdict()
            path = placeholder % group
            try:
                redirect = Redirect.objects.get(originating_url=path)
                if field:
                    redirect.redirect_to_url += group.get(field)
            except Redirect.DoesNotExist:
                pass

        return redirect

    def process_response(self, request, response):

        if response.status_code != 404:
            return response

        full_path = request.get_full_path()
        redirect = None

        logger.debug('full_path = %s', full_path)

        # check to see if there is an existing redirect for the full path as is
        try:
            redirect = Redirect.objects.get(originating_url=full_path)
        except Redirect.DoesNotExist:
            pass

        # try adding a slash if there isn't and see if a redirect exists (may not be necessary)
        if settings.APPEND_SLASH and not request.path.endswith('/'):
            # This scenario should never be reached because CommonMiddleware adds the slash beforehand
            path_len = len(request.path)
            full_path = full_path[:path_len] + '/' + full_path[path_len:]

            try:
                redirect = Redirect.objects.get(originating_url=full_path)
            except Redirect.DoesNotExist:
                pass

        # try removing the trailing slash to see if a redirect is found
        if not redirect and request.path.endswith('/'):
            # try removing the trailing slash to see if a redirect is found
            full_path = request.path[:-1]
            try:
                redirect = Redirect.objects.get(originating_url=full_path)
            except Redirect.DoesNotExist:
                pass

        if not redirect and redirect_settings.URL_MATCH:
            redirect = self.match_pattern(request.get_full_path(), **redirect_settings.URL_MATCH_OPTIONS)

        if not redirect:
            # no existing redirect yet, create it now with the original path that was hit
            redirect = Redirect(originating_url=full_path)
            redirect.save()

        # check for the referer to store a referral
        referer = request.META.get('HTTP_REFERER', redirect_settings.REFERER_NONE_VALUE)
        referral, created = Referral.objects.get_or_create(referer_url=referer, redirect=redirect)
        referral.hits += 1
        referral.last_hit = now()
        referral.save()

        # if default 404 redirect is specified, do a temporary redirect
        if redirect_settings.DEFAULT_404_REDIRECT:
            return http.HttpResponseRedirect(redirect_settings.DEFAULT_404_REDIRECT)

        if redirect.redirect_to_url:
            response_class = self.get_response_class(redirect)
            return response_class(redirect.redirect_to_url)

        # show the 404 page
        return response
