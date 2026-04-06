from django import forms
from .models import ResultadoLaboratorial

class ResultadoLaboratorialForm(forms.ModelForm):
    class Meta:
        model = ResultadoLaboratorial
        # Não incluímos 'amostra', 'data_laudo' e 'fechado' pois o sistema preencherá
        fields = ['p', 'k', 'ca', 'mg', 'h_al', 'argila', 'silte', 'areia']
        
        widgets = {
            'p': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'k': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'ca': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'mg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'h_al': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'argila': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'silte': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'areia': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }