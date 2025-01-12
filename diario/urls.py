from django.urls import path #função path do django para criar urls
from . import views

urlpatterns = [
    path("", views.home),
    path("escrever/", views.escrever, name="escrever"),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name="cadastrar_pessoa")
    
]