from django.shortcuts import render, redirect
from .models import Projeto
from django.http import HttpResponse


# Create your views here.

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'home.html', {'projetos':projetos})

    
