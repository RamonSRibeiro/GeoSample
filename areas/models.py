from django.contrib.gis.db import models

class Fazenda(models.Model):
    nome = models.CharField(max_length=150)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Talhao(models.Model):
    fazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE, related_name='talhoes')
    codigo_talhao = models.CharField(max_length=50, help_text="Ex: Gleba A, Talhão 01")
    area_hectares = models.DecimalField(max_digits=8, decimal_places=2)
    historico_manejo = models.TextField(blank=True, help_text="Registro de intervenções anteriores (calagem, adubação, etc.)")

    def __str__(self):
        return f"{self.fazenda.nome} - {self.codigo_talhao}"

class PontoSondagem(models.Model):
    talhao = models.ForeignKey(Talhao, on_delete=models.CASCADE, related_name='pontos')
    identificador = models.CharField(max_length=50, help_text="Ex: Ponto 01")
    
    # Campo Geoespacial: Armazena a exata Latitude e Longitude
    coordenadas = models.PointField(srid=4326, help_text="Coordenadas geográficas da extração")
    data_marcacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.talhao.codigo_talhao} - {self.identificador}"