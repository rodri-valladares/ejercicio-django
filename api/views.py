from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404

from producto_app.models import Producto
# Create your views here.

def listado_productos(request):
    productos = list(Producto.objects.values())
    return JsonResponse(productos, safe=False)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto,id=producto_id)
    producto_dict = model_to_dict(producto)
    return JsonResponse(producto_dict, safe=False)