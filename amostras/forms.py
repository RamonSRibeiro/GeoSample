from django import forms
from .models import Amostra

class AmostraForm(forms.ModelForm):
    class Meta:
        model = Amostra
        fields = ['ponto_origem', 'codigo_rastreio', 'data_coleta', 'data_limite_analise', 'localizacao_bancada']
        
        # Aplicando as classes do Bootstrap 5 diretamente nos campos do Django
        widgets = {
            'ponto_origem': forms.Select(attrs={'class': 'form-select'}),
            'codigo_rastreio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: GEO-2026-001'}),
            'data_coleta': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'data_limite_analise': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'localizacao_bancada': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Geladeira 1'}),
        }