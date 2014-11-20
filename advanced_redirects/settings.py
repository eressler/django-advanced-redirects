from django.conf import settings

# Options for options list in admin page
PERMANENT_REDIRECT_VALUE = '301'
TEMPORARY_REDIRECT_VALUE = '302'
REDIRECT_CHOICES = (
    (PERMANENT_REDIRECT_VALUE, '301 - Permanent'),
    (TEMPORARY_REDIRECT_VALUE, '302 - Temporary')
)

# Optional setting to specify default redirection for 404 hits if no explicit redirect is provided
DEFAULT_404_REDIRECT = getattr(settings, 'DEFAULT_404_REDIRECT', None)