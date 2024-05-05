from django import forms

class NombreEmpresa(forms.Form):
    nombre = forms.CharField(label='Nombre de la empresa', max_length=100, required=False)
