from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Amostra
from .forms import AmostraForm

@require_POST
def atualizar_status_amostra(request, amostra_id):
    """
    Atualiza o status da amostra via HTMX.
    Retorna apenas o fragmento HTML da linha da tabela.
    """
    amostra = get_object_or_404(Amostra, id=amostra_id)
    novo_status = request.POST.get('novo_status')
    
    # Validação rigorosa baseada nos choices do Model
    if novo_status in dict(Amostra.StatusCustodia.choices):
        amostra.status = novo_status
        amostra.save()
    
    # Importante: O partial deve existir em templates/partials/amostra_linha.html
    return render(request, 'partials/amostra_linha.html', {'amostra': amostra})


class AmostraListView(ListView):
    model = Amostra
    template_name = 'amostras/lista.html'
    context_object_name = 'amostras'
    ordering = ['-data_coleta']


class AmostraCreateView(CreateView):
    model = Amostra
    form_class = AmostraForm
    template_name = 'amostras/form.html'
    success_url = reverse_lazy('lista_amostras')