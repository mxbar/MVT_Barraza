from django.contrib import admin
from django.urls import path
from . import views
from .models import Familiar

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('Lista_Familiares', views.lista_familiares, name="Lista_Familiares"),
]