from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Persona, Empresa, Locacion
from .forms import PersonaForm, LocacionForm, EmpresaForm

#from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'index.html')

# funciones para persona
##
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

def persona_add(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('persona_listar')
    else:
        form = PersonaForm()
    return render (request, 'persona_form.html', {'form':form})

def persona_delete(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona_listar')
    return render(request, 'persona_delete.html', {'persona':persona})


# funciones para empresa
##
def empresa_list(request):
    empresa = Empresa.objects.all()
    contexto = {'empresas':empresa}
    return render(request, 'empresa_list.html', contexto)

def empresa_add(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('empresa_listar')
    else:
        form = EmpresaForm()
    return render (request, 'empresa_form.html', {'form':form})

def empresa_edit(request, id_empresa):
    empresa = Empresa.objects.get(id=id_empresa)
    if request.method == 'GET':
        form = EmpresaForm(instance=empresa)
    else:
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
        return redirect('empresa_listar')
    return render(request, 'empresa_form.html', {'form':form})

def empresa_delete(request, id_empresa):
    empresa = Empresa.objects.get(id=id_empresa)
    if request.method == 'POST':
        empresa.delete()
        return redirect('empresa_listar')
    return render(request, 'empresa_delete.html', {'empresa':empresa})

# funciones para locacion
##
def locacion_list(request):
    locacion = Locacion.objects.all()
    contexto = {'locaciones':locacion}
    return render(request, 'locacion_list.html', contexto)

def locacion_add(request):
    if request.method == 'POST':
        form = LocacionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('locacion_listar')
    else:
        form = LocacionForm()
    return render (request, 'locacion_form.html', {'form':form})

def locacion_edit(request, id_locacion):
    locacion = Locacion.objects.get(id=id_locacion)
    if request.method == 'GET':
        form = LocacionForm(instance=locacion)
    else:
        form = LocacionForm(request.POST, instance=locacion)
        if form.is_valid():
            form.save()
        return redirect('locacion_listar')
    return render(request, 'locacion_form.html', {'form':form})

def locacion_delete(request, id_locacion):
    locacion = Locacion.objects.get(id=id_locacion)
    if request.method == 'POST':
        locacion.delete()
        return redirect('locacion_listar')
    return render(request, 'locacion_delete.html', {'locacion':locacion})
