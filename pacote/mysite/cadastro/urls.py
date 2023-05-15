from django.urls import path

from . import views
app_name = 'cadastro'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('cadastradas', views.cadastradas, name='cadastradas')
]