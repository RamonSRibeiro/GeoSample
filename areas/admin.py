from django.contrib.gis import admin
from .models import Fazenda, Talhao, PontoSondagem

@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'municipio', 'estado', 'data_cadastro')
    search_fields = ('nome', 'municipio')

@admin.register(Talhao)
class TalhaoAdmin(admin.ModelAdmin):
    list_display = ('codigo_talhao', 'fazenda', 'area_hectares')
    list_filter = ('fazenda',)
    search_fields = ('codigo_talhao',)

@admin.register(PontoSondagem)
class PontoSondagemAdmin(admin.GISModelAdmin):
    # O GISModelAdmin renderiza automaticamente um mapa (OpenStreetMap) para o PointField
    list_display = ('identificador', 'talhao', 'data_marcacao')
    list_filter = ('talhao__fazenda', 'talhao')
    search_fields = ('identificador',)
    
    # Configurações do mapa no painel admin
    default_lat = -15.7801 # Latitude padrão (ex: Brasil)
    default_lon = -47.9292 # Longitude padrão
    default_zoom = 4