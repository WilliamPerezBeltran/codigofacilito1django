
from django.contrib import admin
from django.urls import path,include
from apps.adopcion import views

urlpatterns = [
	path("",views.index_adopcion, name="index_adopcion")
]
