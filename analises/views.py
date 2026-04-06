from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from amostras.models import Amostra
from .models import ResultadoLaboratorial
from .forms import ResultadoLaboratorialForm

def registrar_analise(request, amostra_id):
    # Busca a amostra a qual este laudo pertence
    amostra = get_object_or_404(Amostra, id=amostra_id)
    
    # Busca um resultado existente ou inicializa um novo
    resultado, created = ResultadoLaboratorial.objects.get_or_create(amostra=amostra)
    
    if request.method == 'POST':
        # Se o laudo já foi fechado (auditado), bloqueia a edição
        if resultado.fechado:
            messages.error(request, "Este laudo já foi fechado e não pode ser alterado.")
            return redirect('lista_amostras')
            
        form = ResultadoLaboratorialForm(request.POST, instance=resultado)
        if form.is_valid():
            form.save()
            messages.success(request, f"Resultados para {amostra.codigo_rastreio} salvos com sucesso!")
            return redirect('lista_amostras')
    else:
        form = ResultadoLaboratorialForm(instance=resultado)
        
    context = {
        'form': form,
        'amostra': amostra,
        'resultado': resultado
    }
    return render(request, 'analises/form_resultado.html', context)