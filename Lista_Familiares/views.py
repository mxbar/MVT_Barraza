from django.shortcuts import render
from .models import Familiar
# Create your views here.

def inicio(request):
    return render(request, 'Lista_Familiares/inicio.html', {})

def lista_familiares(request):
    familiar = Familiar.objects.all()
    return render(request, 'Lista_Familiares/lista_familiares.html', {'familiar' : familiar})