from django.shortcuts import render,redirect
from articulos.models import Articulos

def lista_articulos(request):
    articulos=Articulos.objects.all()

    return render(request,'articulos.html',{'articulos':articulos})

def eliminar_articulos(request,id):
    Articulos.objects.get(id=id).delete()
    return redirect('lista_articulos')
