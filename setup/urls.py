"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from areas.views import dashboard 
from amostras.views import atualizar_status_amostra, AmostraListView, AmostraCreateView
from analises.views import registrar_analise
from areas.views import dashboard, FazendaListView, FazendaCreateView, PontoSondagemCreateView, TalhaoCreateView
from amostras.views import exportar_laudos_excel
from amostras.views import gerar_laudo_pdf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('amostras/atualizar-status/<int:amostra_id>/', atualizar_status_amostra, name='atualizar_status_amostra'), # <--- Rota da página inicial
    path('amostras/', AmostraListView.as_view(), name='lista_amostras'),
    path('amostras/nova/', AmostraCreateView.as_view(), name='nova_amostra'),
    path('amostras/atualizar-status/<int:amostra_id>/', atualizar_status_amostra, name='atualizar_status_amostra'),
    path('amostras/<int:amostra_id>/analise/', registrar_analise, name='registrar_analise'),
    path('fazendas/', FazendaListView.as_view(), name='lista_fazendas'),
    path('fazendas/nova/', FazendaCreateView.as_view(), name='nova_fazenda'),
    path('pontos/novo/', PontoSondagemCreateView.as_view(), name='novo_ponto'),
    path('talhoes/novo/', TalhaoCreateView.as_view(), name='novo_talhao'),
    path('exportar-laudos/', exportar_laudos_excel, name='exportar_laudos'),
    path('amostra/<str:amostra_id>/laudo-pdf/', gerar_laudo_pdf, name='gerar_laudo_pdf')

]