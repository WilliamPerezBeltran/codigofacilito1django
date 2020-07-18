
from django.contrib import admin
from django.urls import path,include
# from . import views
from apps.mascota import views

app_name ='mascota'

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'nuevo', views.mascota_view, name="mascota_new"),
    path(r'crear', views.mascota_crear, name="mascota_crear"),
    path(r'listar', views.mascota_listar, name="mascota_listar"),
    path(r'editar/<int:id_mascota>/', views.mascota_editar, name="mascota_editar"),
    path(r'eliminar/<int:id_mascota>/', views.mascota_eliminar, name="mascota_eliminar"),
]


