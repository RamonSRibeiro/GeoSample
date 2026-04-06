from django.shortcuts import render
from .models import PontoSondagem, Fazenda
from amostras.models import Amostra

def dashboard(request):
    # Coletando métricas rápidas para os cards
    total_fazendas = Fazenda.objects.count()
    amostras_em_processo = Amostra.objects.exclude(status='FI').count()
    pontos_coleta = PontoSondagem.objects.all()
    amostras_recentes = Amostra.objects.all().order_by('-data_coleta')[:10]

    context = {
        'total_fazendas': total_fazendas,
        'amostras_em_processo': amostras_em_processo,
        'pontos_coleta': pontos_coleta,
        'amostras': amostras_recentes,
    }
    return render(request, 'dashboard.html', context)

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Fazenda, PontoSondagem
from .forms import FazendaForm, PontoSondagemForm



class FazendaListView(ListView):
    model = Fazenda
    template_name = 'areas/lista_fazendas.html'
    context_object_name = 'fazendas'

class FazendaCreateView(CreateView):
    model = Fazenda
    form_class = FazendaForm
    template_name = 'areas/form_fazenda.html'
    success_url = reverse_lazy('lista_fazendas')

class PontoSondagemCreateView(CreateView):
    model = PontoSondagem
    form_class = PontoSondagemForm
    template_name = 'areas/form_ponto.html'
    success_url = reverse_lazy('dashboard') 

from .models import Fazenda, Talhao, PontoSondagem
from .forms import FazendaForm, TalhaoForm, PontoSondagemForm



class TalhaoCreateView(CreateView):
    model = Talhao
    form_class = TalhaoForm
    template_name = 'areas/form_talhao.html'
    success_url = reverse_lazy('dashboard')