from typing import Any, Dict
from django import forms

from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length="100")
    password = forms.CharField(label="Password", max_length="100", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", max_length="100", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email", max_length="100")
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise ValidationError("Password fields do not match.")


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length="100")
    password = forms.CharField(label="Password", max_length="100", widget=forms.PasswordInput)