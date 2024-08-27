from django import forms
from .models import Cliente, Servicios, Consultas

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = '__all__'

class ConsultasForm(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = '__all__'
