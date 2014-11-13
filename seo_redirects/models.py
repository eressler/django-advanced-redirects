from django.db import models
from seo_redirects import settings


class SeoRedirect (models.Model):
    """
    Store page paths that require redirects to new pages.
    """
    class Meta:
        ordering = ('-last_hit', '-hits', 'originating_url')

    originating_url = models.CharField(
        max_length=1000,
        unique=True,
        help_text='The originating URL that triggered a 404 error or is manually entered.'
    )
    redirect_to_url = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        help_text='Optional. Specify the to which the originating URL should redirect. This should be an absolute or root-relative URL.'
    )
    redirect_type = models.CharField(
        choices=settings.REDIRECT_CHOICES,
        default=settings.REDIRECT_CHOICES[0][0]
    )
    hits = models.PositiveIntegerField(
        default=0,
        help_text='The number of times the originating URL has been hit.'
    )
    last_hit = models.DateTimeField(
        help_text='The last time the originating URL was hit.',
        blank=True,
        null=True
    )