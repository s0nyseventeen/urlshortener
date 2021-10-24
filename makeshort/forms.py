from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class UrlForm(forms.Form):
    url = forms.CharField(label='Full URL')

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get('url')
        url_validator = URLValidator()
        try:
            url_validator(url)
        except Exception:
            raise forms.ValidationError("Invalid URL")
        return url
