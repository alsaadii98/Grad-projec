from django import forms
from .models import PasswordsManger
from django.contrib.auth.hashers import make_password


class PasswordForm(forms.ModelForm):
    site_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter The Website Name'}))
    site_url = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the Website URL'}))
    site_username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter The Username'}))
    site_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter The Password'}))

    class Meta:
        model = PasswordsManger
        fields = [
            'site_name',
            'site_url',
            'site_username',
            'site_password',
        ]

    def clean_site_password(self):
        un_hash_password = self.cleaned_data.get('site_password')
        hashed_password = make_password(un_hash_password, 'some_slat')
        return hashed_password
