from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
#from django.template import loader


# Create your views here.
def index(request):
    return render(request, 'index.html')

def persona_list(request):
    persona = Persona.objects.all()
    contexto = {'personas':persona}
    return render(request, 'persona_list.html', contexto)

def persona_album(request):
    persona = Persona.objects.all()
    contexto = {'personas':persona}
    return render(request, 'persona_album.html', contexto)
