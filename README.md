# GeoSample Analytics

Sistema Django para gestão e rastreabilidade geográfica de amostras agronômicas. O projeto organiza fazendas, talhões, pontos de sondagem com coordenadas geográficas, controla o ciclo de custódia das amostras e registra resultados laboratoriais.

## Funcionalidades principais

- Dashboard de monitoramento com totais de fazendas, amostras em processo e pontos de coleta.
- Cadastro de fazendas, talhões e pontos de sondagem.
- Registro de amostras com código de rastreio, data de coleta, local de bancada e status de custódia.
- Atualização de status de amostras via formulário/HTMX.
- Cadastro de resultados laboratoriais para cada amostra.
- Cálculo automático de Soma de Bases (SB), Capacidade de Troca Catiônica (CTC) e Saturação por Bases (V%).
- Exportação de relatórios de amostras em formato CSV compatível com Excel.

## Tecnologias

- Python 3
- Django 6.0
- GeoDjango / PostGIS
- pandas, openpyxl para exportação de dados

## Estrutura do projeto

- `setup/` - configuração do projeto Django (settings, urls, wsgi, asgi)
- `areas/` - modelos e views de fazenda, talhão e ponto de sondagem
- `amostras/` - modelos e views de amostra, atualização de status e exportação de laudos
- `analises/` - modelos e views de resultados laboratoriais
- `templates/` - templates de interface e formulários
- `requirements.txt` - dependências do Python

## Requisitos

- Python 3.11+ (ou 3.10 compatível)
- PostgreSQL com extensão PostGIS
- Virtualenv recomendado

## Instalação

```bash
cd /home/ramon/Área de Trabalho/geosample_analytics
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuração do banco de dados

O projeto está configurado para usar PostGIS no arquivo `setup/settings.py`:

- `ENGINE`: `django.contrib.gis.db.backends.postgis`
- `NAME`: `geosample`
- `USER`: `geo_user`
- `PASSWORD`: `geo_pass`
- `HOST`: `localhost`
- `PORT`: `5432`

Ajuste esses valores conforme seu ambiente se necessário.

### Criar banco de dados (exemplo)

```bash
sudo -u postgres createdb geosample
sudo -u postgres createuser -P geo_user
sudo -u postgres psql -c "grant all privileges on database geosample to geo_user;"
```

Certifique-se de habilitar PostGIS no banco:

```bash
sudo -u postgres psql -d geosample -c "CREATE EXTENSION postgis;"
```

## Migrações e execução

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abra `http://127.0.0.1:8000/` no navegador.

## Rotas principais

- `/` - dashboard
- `/amostras/` - lista de amostras
- `/amostras/nova/` - cadastrar amostra
- `/amostras/<id>/analise/` - registrar resultado laboratorial
- `/fazendas/` - lista de fazendas
- `/fazendas/nova/` - cadastrar fazenda
- `/pontos/novo/` - cadastrar ponto de sondagem
- `/talhoes/novo/` - cadastrar talhão
- `/exportar-laudos/` - exportar relatório CSV

## Observações

- O projeto usa GeoDjango, portanto o banco de dados deve suportar PostGIS.
- O campo `coordenadas` em `PontoSondagem` é um `PointField` geoespacial.
- A exportação gera CSV com separador `;` e BOM UTF-8 para compatibilidade com Excel.

