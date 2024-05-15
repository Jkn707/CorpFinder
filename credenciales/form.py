from django import forms
from django.contrib.auth.models import User
from .models import Credenciales

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CredencialForm(forms.ModelForm):
    class Meta:
        model = Credenciales
        fields = ['imagen','redes','CV']  