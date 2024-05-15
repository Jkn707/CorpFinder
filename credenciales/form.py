from django import forms

class MostrarTextoForm(forms.Form):
    mostrar_input = forms.BooleanField(required=False)
    texto = forms.CharField(max_length=100, required=False)
    