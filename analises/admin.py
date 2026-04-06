from django.contrib import admin
from .models import ResultadoLaboratorial

@admin.register(ResultadoLaboratorial)
class ResultadoLaboratorialAdmin(admin.ModelAdmin):
    list_display = ('amostra', 'data_laudo', 'get_ctc', 'get_v_porcento', 'fechado')
    list_filter = ('fechado', 'data_laudo')
    search_fields = ('amostra__codigo_rastreio',)
    
    # Impede edição de campos calculados dinamicamente
    readonly_fields = ('get_soma_bases', 'get_ctc', 'get_v_porcento', 'data_laudo')
    
    fieldsets = (
        ('Identificação', {
            'fields': ('amostra', 'fechado', 'data_laudo')
        }),
        ('Macronutrientes e Acidez (cmolc/dm³)', {
            'fields': ('p', 'k', 'ca', 'mg', 'h_al')
        }),
        ('Índices Calculados (Automático)', {
            'fields': ('get_soma_bases', 'get_ctc', 'get_v_porcento'),
            'description': "Estes valores são calculados automaticamente com base na química inserida."
        }),
        ('Granulometria (%)', {
            'fields': ('argila', 'silte', 'areia')
        }),
    )

    # Funções para encapsular as properties do modelo
    def get_soma_bases(self, obj): return round(obj.soma_bases, 2)
    get_soma_bases.short_description = 'Soma de Bases (SB)'

    def get_ctc(self, obj): return round(obj.ctc, 2)
    get_ctc.short_description = 'CTC'

    def get_v_porcento(self, obj): return f"{round(obj.v_porcento, 2)}%"
    get_v_porcento.short_description = 'Saturação (V%)'

    def get_readonly_fields(self, request, obj=None):
        # Proteção de Auditoria: Se o laudo estiver fechado, bloqueia edição de tudo
        if obj and obj.fechado:
            return [f.name for f in self.model._meta.fields] + list(self.readonly_fields)
        return self.readonly_fields