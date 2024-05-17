from django import forms
from django.contrib.auth.models import User
from .models import Credenciales
from .widgets import CustomClearableFileInput
class UserForm(forms.ModelForm):
    new_password = forms.CharField(required=False, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and new_password != confirm_password:
            raise forms.ValidationError("The new passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get("new_password")
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return user

class CredencialForm(forms.ModelForm):
    class Meta:
        model = Credenciales
        fields = ['imagen', 'redes', 'CV']  
        widgets = {
            'imagen': CustomClearableFileInput,
        }
