from django import forms
from seo_redirects.models import SeoRedirect


class SeoRedirectAdminForm(forms.ModelForm):
    class Meta:
        model = SeoRedirect