import hashlib
from django.db import models
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

from . import settings


class Redirect(models.Model):
    """
    Store page paths that require redirects to new pages.
    """
    class Meta:
        ordering = ('originating_url',)
        verbose_name = _('redirect')
        verbose_name_plural = _('redirects')

    id = models.CharField(max_length=129, primary_key=True, editable=True)
    originating_url = models.CharField(
        max_length=255,
        help_text='The originating URL that triggered a 404 error or is manually entered.'
    )
    redirect_to_url = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Optional. Specify the URL to which the originating URL should redirect. This should be an absolute or root-relative URL.'
    )
    redirect_type = models.CharField(
        max_length=10,
        choices=settings.REDIRECT_CHOICES,
        default=settings.REDIRECT_CHOICES[0][0]
    )

    def __str__(self):
        return "%s ---> %s" % (self.originating_url[:50], self.redirect_to_url)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.originating_url = smart_text(self.originating_url)
        self.id = hashlib.sha256(self.originating_url.encode('utf-8')).hexdigest()
        super(Redirect, self).save(force_insert, force_update, using, update_fields)


class Referral (models.Model):
    """
    Stores the referer from the request headers that directed to the url that generated a 404 error.
    This can be useful for identifying who is linking to pages that do not exist.
    """
    class Meta:
        ordering = ('-hits',)

    redirect = models.ForeignKey(
        Redirect,
        related_name='referrals'
    )
    referer_url = models.CharField(
        max_length=1000,
        help_text='The URL of the previous page that redirected to this url that generated the 404 error.'
    )
    hits = models.PositiveIntegerField(
        default=0,
        help_text='The number of times the originating URL has been hit.'
    )
    last_hit = models.DateTimeField(
        blank=True,
        null=True,
        help_text='The last time the originating URL was hit.'
    )

    def reset_hit_counts(self):
        self.hits = 0
        self.last_hit = None
        self.save()
