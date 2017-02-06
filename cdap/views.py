from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Persona, Empresa, Locacion
from .forms import PersonaForm

#from django.template import loader


# Create your views here.
def index(request):
    return render(request, 'index.html')

# funciones para persona
## listado
def persona_list(request):
    persona = Persona.objects.all()
    contexto = {'personas':persona}
    return render(request, 'persona_list.html', contexto)

def persona_album(request):
    persona = Persona.objects.all()
    contexto = {'personas':persona}
    return render(request, 'persona_album.html', contexto)

def persona_edit(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'GET':
        form = PersonaForm(instance=persona)
    else:
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
        return redirect('persona_listar')
    return render(request, 'persona_form.html', {'form':form})


## formulario para agregar una persona
def persona_add(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('cdap:index')
    else:
        form = PersonaForm()
    return render (request, 'persona_form.html', {'form':form})





# funciones para empresa
def empresa_list(request):
    empresa = Empresa.objects.all()
    contexto = {'empresas':empresa}
    return render(request, 'empresa_list.html', contexto)


# funciones para locacion
def locacion_list(request):
    locacion = Locacion.objects.all()
    contexto = {'locaciones':locacion}
    return render(request, 'locacion_list.html', contexto)
