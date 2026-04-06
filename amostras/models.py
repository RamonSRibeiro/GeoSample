from django.db import models
from areas.models import PontoSondagem
from datetime import timedelta
from django.utils import timezone

class Amostra(models.Model):
    # Enumeração de estágios do fluxo de trabalho científico
    class StatusCustodia(models.TextChoices):
        COLETADO = 'CO', 'Coletado'
        SECAGEM = 'SE', 'Em Secagem'
        MOAGEM = 'MO', 'Em Moagem'
        ANALISE = 'AN', 'Em Análise'
        FINALIZADO = 'FI', 'Finalizado'
        DESCARTADO = 'DE', 'Descartado'

    ponto_origem = models.ForeignKey(PontoSondagem, on_delete=models.PROTECT, related_name='amostras')
    codigo_rastreio = models.CharField(max_length=100, unique=True)
    
    status = models.CharField(max_length=2, choices=StatusCustodia.choices, default=StatusCustodia.COLETADO)
    localizacao_bancada = models.CharField(max_length=150, help_text="Ex: Estufa 02, Prateleira C", blank=True)
    
    data_coleta = models.DateTimeField()
    data_limite_analise = models.DateTimeField(help_text="Tempo de retenção máximo antes da análise química")

    def __str__(self):
        return self.codigo_rastreio

    @property
    def amostra_vencida(self):
        """Retorna True se a amostra passou da data limite e ainda não foi finalizada."""
        if self.status not in [self.StatusCustodia.FINALIZADO, self.StatusCustodia.DESCARTADO]:
            return timezone.now() > self.data_limite_analise
        return False