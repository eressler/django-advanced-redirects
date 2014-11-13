from django.contrib import admin
from seo_redirects.forms import SeoRedirectAdminForm
from seo_redirects.models import SeoRedirect


class HasRedirectListFilter(admin.SimpleListFilter):
    """
    Custom list filter so that the redirects can be filtered by whether a url already has a redirect or not
    """
    title = "Has a redirect"
    parameter_name = "has_redirect"

    def lookups(self, request, model_admin):
        return (
            ('true', 'True'),
            ('false', 'False')
        )

    def queryset(self, request, queryset):
        if self.value() == 'true':
            return queryset.filter(redirect_to_url__isnull=False)
        if self.value() == 'false':
            return queryset.filter(redirect_to_url__isnull=True)


class SeoRedirectAdmin (admin.ModelAdmin):
    form = SeoRedirectAdminForm
    fields = ('originating_url', 'redirect_to_url', 'redirect_type', 'hits', 'last_hit')
    list_display = ('originating_url', 'redirect_to_url', 'redirect_type', 'hits', 'last_hit')
    list_editable = ('redirect_to_url', 'redirect_type')
    list_filter = (HasRedirectListFilter,)
    search_fields = ('originating_url', 'redirect_to_url')

admin.site.register(SeoRedirect, SeoRedirectAdmin)