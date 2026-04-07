from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from amostras.models import Amostra
from analises.models import ResultadoLaboratorial

from .models import Amostra
from .forms import AmostraForm


def gerar_laudo_pdf(request, amostra_id):
    amostra = get_object_or_404(Amostra, id=amostra_id)
    
    analise = ResultadoLaboratorial.objects.filter(amostra=amostra).first()
    
    template_path = 'amostras/laudo_pdf.html'
    
    context = {'amostra': amostra, 'analise': analise}
    
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Erro ao gerar o PDF', status=500)
    
    return response

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


import csv
from django.http import HttpResponse
from amostras.models import Amostra

def exportar_laudos_excel(request):
    # Configura o arquivo para ser um CSV lido perfeitamente pelo Excel
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rastreio_amostras.csv"'
    response.write(u'\ufeff'.encode('utf8')) 
    
    writer = csv.writer(response, delimiter=';')

    # 1. As exatas 5 colunas que você solicitou
    writer.writerow([
        'UID / CÓDIGO', 
        'PONTO DE ORIGEM', 
        'ESTÁGIO ATUAL', 
        'BANCADA / SETOR', 
        'CONTROLES DE FLUXO'
    ])

    amostras = Amostra.objects.select_related('ponto_origem').all()
    
    for amostra in amostras:
        # Lógica para o controle de fluxo usando a sua propriedade @property
        if amostra.status in ['FI', 'DE']:
            controle = "Encerrada"
        elif amostra.amostra_vencida:
            controle = "Atrasada (Vencida)"
        else:
            controle = "No Prazo"

        # Lógica para mostrar algo se a bancada estiver vazia
        bancada = amostra.localizacao_bancada if amostra.localizacao_bancada else 'Não Alocado'

        # 3. Escreve a linha usando OS NOMES EXATOS DO SEU MODEL
        writer.writerow([
            amostra.codigo_rastreio,             # Seu UID
            str(amostra.ponto_origem),           # A ForeignKey do Ponto
            amostra.get_status_display(),        # Pega o texto 'Em Secagem', 'Finalizado', etc
            bancada,                             # A sua localizacao_bancada
            controle                             # O status de atraso que acabamos de calcular
        ])

    return response