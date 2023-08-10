from django import forms
from .models import Tienda

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ['nombre', 'direccion', 'telefono', 'email', 'web', 'descripcion']