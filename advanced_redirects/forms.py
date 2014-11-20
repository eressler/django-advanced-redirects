from django import forms

from .models import Redirect


class RedirectAdminForm(forms.ModelForm):
    class Meta:
        model = Redirect
        exclude = ()