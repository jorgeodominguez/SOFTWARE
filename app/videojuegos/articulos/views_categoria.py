from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from articulos.models import Articulos, Categoria

class ListaCategorias(ListView):
    model=Categoria

class nuevaCategoriaView(CreateView):
    model=Categoria
    fields='__all__'
    success_url=reverse_lazy('categorias_list')

class editarCategoriaView(UpdateView):
    model=Categoria
    fields='__all__'
    success_url=reverse_lazy('categorias_list')

class eliminarCategoriaView(DeleteView):
    model=Categoria
    fields='__all__'
    success_url=reverse_lazy('categorias_list')

class BienvenidaView(TemplateView):
    template_name='bienvenida.html'