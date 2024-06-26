from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from webscraping.models import ComentariosPropios

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    Tipo = forms.ChoiceField(choices=[('Empresa','Empresa'), ('Persona', 'Persona')])

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = ComentariosPropios
        fields = ('contenido', 'calificacion')
        widgets = {
            'calificacion': forms.NumberInput(attrs={'min': '0', 'max': '5'}),
        }

