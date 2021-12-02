from django.shortcuts import render, redirect
from django.http import HttpResponse
from inventario.models import Producto



def list(request):
    productos = Producto.objects.all()
    return render(request, 'catalogue.html',{"lista":productos })

def save(request):
    if request.method == "GET":
        return render(request, 'agregar_Celular.html')
    name_ = request.POST["name"]
    description_ = request.POST["description"]
    price_ = request.POST["price"]
    file_ = request.FILES["archivo"]

    producto = Producto(name= name_, description= description_, price= price_, image= file_)
    producto.save()

    return redirect('catalogoProductos')

def contact(request):
    return render(request, 'contactanos.html')

def index(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'agregar.html')


