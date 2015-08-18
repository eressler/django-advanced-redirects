from django.contrib import admin, messages
from .forms import RedirectAdminForm
from .models import Redirect, Referral


def delete_referers(self, request, queryset):
    for redirect in queryset:
        redirect.referrals.all().delete()
    messages.success(request, "All referers for the selected redirects were successfully deleted.")
delete_referers.short_description = "Delete all referers for selected redirects"


def reset_referer_hit_counts(self, request, queryset):
    for redirect in queryset:
        redirect.referrals.all().update(hits=0, last_hit=None)
    messages.success(request, "All referer hit counts for the selected redirects were successfully reset.")
reset_referer_hit_counts.short_description = "Reset all referer hit counts for selected redirects"


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


class ReferralInlineAdmin(admin.TabularInline):
    """
    Non-editable inline displays the referrals information.
    """
    model = Referral
    extra = 0

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return ['referer_url', 'hits', 'last_hit']


@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    """
    The main admin functionality for the Redirects model. Slightly customized.
    """
    class Media:
        css = {'all': ('advanced_redirects/hide_inline_header.css',)}

    form = RedirectAdminForm
    fields = ('originating_url', 'redirect_to_url', 'redirect_type',)
    list_display = ('get_originating_url', 'redirect_to_url', 'redirect_type', 'get_hits')
    list_editable = ('redirect_to_url', 'redirect_type')
    list_filter = (HasRedirectListFilter,)
    search_fields = ('originating_url', 'redirect_to_url')
    inlines = (ReferralInlineAdmin,)
    actions = [delete_referers, reset_referer_hit_counts]

    def get_originating_url(self, obj):
        return "%s" % obj.originating_url[:100]
    get_originating_url.short_description = 'URL'

    def get_hits(self, obj):
        """Return referrals quantity for the instance."""
        return sum(obj.referrals.all().values_list('hits', flat=True))
