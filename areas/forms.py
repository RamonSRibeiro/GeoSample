from django import forms
from .models import Fazenda, PontoSondagem
from .models import Fazenda, Talhao, PontoSondagem


class FazendaForm(forms.ModelForm):
    class Meta:
        model = Fazenda
        fields = ['nome', 'municipio', 'estado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da propriedade'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF'}),
        }

class PontoSondagemForm(forms.ModelForm):
    # Campo oculto que receberá o texto WKT (Well-Known Text) gerado pelo clique no mapa
    coordenadas = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'id_coordenadas'}))

    class Meta:
        model = PontoSondagem
        fields = ['talhao', 'identificador', 'coordenadas']
        widgets = {
            'talhao': forms.Select(attrs={'class': 'form-select'}),
            'identificador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Ponto 01'}),
        }

class TalhaoForm(forms.ModelForm):
    class Meta:
        model = Talhao
        fields = ['fazenda', 'codigo_talhao', 'area_hectares', 'historico_manejo']
        widgets = {
            'fazenda': forms.Select(attrs={'class': 'form-select'}),
            'codigo_talhao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Gleba Sul - Talhão 02'}),
            'area_hectares': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Tamanho em hectares'}),
            'historico_manejo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva o histórico de culturas, última calagem, adubação, etc.'}),
        }