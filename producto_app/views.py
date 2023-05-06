from django.shortcuts import render
from django.http import HttpResponse

from producto_app.models import Marca
# Create your views here.
def index(request):
    return HttpResponse('Hola mundo!')

# def ejemplo_template(request):
#     context = {
#         "nombre":"Rodrigo",
#         "apellido":"Valladares",
#         "curso":"Django",
#     }
#     return render(request,"producto_app/ejemplo.html",context)

def ejemplo_template(request):
    marcas = Marca.objects.get(nombre="cx") #pusimos un get a proposito, para que no funcione
    return render(request,"producto_app/ejemplo.html",{"marcas": marcas})