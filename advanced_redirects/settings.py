from django.conf import settings

# Options for options list in admin page
PERMANENT_REDIRECT_VALUE = '301'
TEMPORARY_REDIRECT_VALUE = '302'
REDIRECT_CHOICES = (
    (PERMANENT_REDIRECT_VALUE, '301 - Permanent'),
    (TEMPORARY_REDIRECT_VALUE, '302 - Temporary')
)

# default string name to use for 404s that don't provide a referer value in the request headers
REFERER_NONE_VALUE = '(no referer)'

# Optional setting to specify default redirection for 404 hits if no explicit redirect is provided
DEFAULT_404_REDIRECT = getattr(settings, 'DEFAULT_404_REDIRECT', None)

# Optional setting to check urls pattern
URL_MATCH = getattr(settings, 'REDIRECT_URL_MATCH', False)

URL_MATCH_OPTIONS = getattr(settings, 'REDIRECT_URL_MATCH_OPTIONS', {})
