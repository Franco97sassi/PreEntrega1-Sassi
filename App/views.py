from django.shortcuts import render
from django.http import HttpResponse
from App.forms import RegistroFormulario, RegistroPersona, RegistroIntegrantes
from App.models import Persona, Registro, Integrantes
from django.template import loader
 # Create your views here.

def inicio(request):
    return render(request, "App/inicio.html")

def nosotros(request):
    return render(request, "App/nosotros.html")

def registro(request):
    if request.method == "POST":
        formulario = RegistroFormulario(request.POST)
        print(formulario)
        if formulario.is_valid():
            data = formulario.cleaned_data
            registro = Registro(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            registro.save()
         
    else:
        formulario= RegistroFormulario()

    return render(request, "App/registro.html", {"formulario": formulario})

def personaFormulario(request):
    if request.method == "POST":
        formulario = RegistroPersona(request.POST)
        print(formulario)
        if formulario.is_valid():
            data = formulario.cleaned_data
            persona = Persona(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], Nacimiento=data["Nacimiento"])

            persona.save()
    else:
        formulario = RegistroPersona()

    return render(request, "App/personaFormulario.html", {"formulario": formulario})

def listadoTrabajadores(request):
    if request.method == "POST":
        formulario = RegistroIntegrantes(request.POST)
        print(formulario)
        if formulario.is_valid():
            data = formulario.cleaned_data
            integrante = Integrantes(nombre=data["nombre"], apellido=data["apellido"], profesion=data["profesion"])

            integrante.save()
    else:
        formulario = RegistroIntegrantes()

    return render(request, "App/Integrantes_empresa.html", {"formulario": formulario})
def buscarPersonas(request):
    return render(request, "App/buscarPersonas.html")

def buscar(request):
    if request.GET["apellido"]:
        apellido = request.GET['apellido']
        personas = Persona.objects.filter(apellido__icontains=apellido)
        return render(request, "App/resultadosBuscar.html", {"personas":personas ,apellido:"apellido"})
    else:
        respuesta="no enviaste datos"
    return HttpResponse(respuesta)