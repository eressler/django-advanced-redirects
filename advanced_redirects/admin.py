from django.contrib import admin

from .forms import RedirectAdminForm
from .models import Redirect


class HasRedirectListFilter(admin.SimpleListFilter):
    """
    Custom list filter so that the items can be filtered by whether a url already has a redirect or not
    """
    title = "has redirect"
    parameter_name = "has_redirect"

    def lookups(self, request, model_admin):
        return (
            (False, 'Yes'),
            (True, 'No')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(redirect_to_url__isnull=self.value())


class RedirectAdmin (admin.ModelAdmin):
    form = RedirectAdminForm
    fields = ('originating_url', 'redirect_to_url', 'redirect_type', 'hits', 'last_hit')
    list_display = ('originating_url', 'redirect_to_url', 'redirect_type', 'hits', 'last_hit')
    list_editable = ('redirect_to_url', 'redirect_type')
    list_filter = (HasRedirectListFilter,)
    search_fields = ('originating_url', 'redirect_to_url')

admin.site.register(Redirect, RedirectAdmin)