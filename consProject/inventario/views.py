from django.shortcuts import render
from django.http import HttpResponse
from inventario.models import Categoria, Producto


def list(request):
    productos = Producto.objects.all()
    list = Categoria.objects.all()
    return render(request, 'inventario/index.html',{"categorias":list, "productos":productos })
