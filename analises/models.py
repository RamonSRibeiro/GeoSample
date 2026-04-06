from django.db import models
from amostras.models import Amostra

class ResultadoLaboratorial(models.Model):
    # Cada amostra tem exatamente um resultado (OneToOne)
    amostra = models.OneToOneField(Amostra, on_delete=models.CASCADE, related_name='resultado')
    
    # Macronutrientes e Acidez (Valores em cmolc/dm³)
    p = models.DecimalField("Fósforo (P)", max_digits=6, decimal_places=2, default=0)
    k = models.DecimalField("Potássio (K)", max_digits=6, decimal_places=2, default=0)
    ca = models.DecimalField("Cálcio (Ca)", max_digits=6, decimal_places=2, default=0)
    mg = models.DecimalField("Magnésio (Mg)", max_digits=6, decimal_places=2, default=0)
    h_al = models.DecimalField("Acidez Potencial (H+Al)", max_digits=6, decimal_places=2, default=0)
    
    # Granulometria (%)
    argila = models.DecimalField("Argila (%)", max_digits=5, decimal_places=2, default=0)
    silte = models.DecimalField("Silte (%)", max_digits=5, decimal_places=2, default=0)
    areia = models.DecimalField("Areia (%)", max_digits=5, decimal_places=2, default=0)
    
    data_laudo = models.DateTimeField(auto_now_add=True)
    fechado = models.BooleanField(default=False, help_text="Se True, bloqueia edições para garantir auditoria.")

    def __str__(self):
        return f"Laudo: {self.amostra.codigo_rastreio}"

    @property
    def soma_bases(self):
        """Cálculo da Soma de Bases (SB)"""
        return self.ca + self.mg + self.k

    @property
    def ctc(self):
        """Cálculo da Capacidade de Troca Catiônica (CTC)"""
        return self.soma_bases + self.h_al

    @property
    def v_porcento(self):
        """Cálculo da Saturação por Bases (V%)"""
        ctc_atual = self.ctc
        if ctc_atual > 0:
            return (self.soma_bases / ctc_atual) * 100
        return 0