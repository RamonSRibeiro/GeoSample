from django.contrib import admin
from .models import Amostra

@admin.register(Amostra)
class AmostraAdmin(admin.ModelAdmin):
    list_display = ('codigo_rastreio', 'ponto_origem', 'status', 'localizacao_bancada', 'exibe_vencida')
    list_filter = ('status', 'data_coleta')
    search_fields = ('codigo_rastreio', 'localizacao_bancada')
    date_hierarchy = 'data_coleta'
    
    # Ações em lote para o laboratório
    actions = ['marcar_em_analise', 'marcar_finalizado']

    def exibe_vencida(self, obj):
        # Exibe um alerta visual se a amostra passou do prazo
        return "⚠️ Sim" if obj.amostra_vencida else "Não"
    exibe_vencida.short_description = "Vencida?"

    @admin.action(description='Mover amostras selecionadas para "Em Análise"')
    def marcar_em_analise(self, request, queryset):
        queryset.update(status=Amostra.StatusCustodia.ANALISE)

    @admin.action(description='Finalizar amostras selecionadas')
    def marcar_finalizado(self, request, queryset):
        queryset.update(status=Amostra.StatusCustodia.FINALIZADO)