from django.shortcuts import render
from django.urls import reverse_lazy # type: ignore
from detalle_compras.models import Detalle_compra
from django.views.generic import ListView,TemplateView # type: ignore
from django.views.generic.edit import CreateView,UpdateView,DeleteView # type: ignore
from detalle_compras.forms import Form_detalle_compra,Form_compra,Form_proveedor,Form_articulo,Form_marca
from detalle_compras.models import Detalle_compra,Proveedor,Compra,Articulo,Marca

#detalle_compra

class BienvenidaView(TemplateView):
    template_name='bienvenida.html'

class Lista_detalle_compras(ListView):
    model=Detalle_compra

class nuevo_detalle_compras(CreateView):
    model=Detalle_compra
    form_class=Form_detalle_compra
    success_url=reverse_lazy('list_detalle_compras')
    extra_context={'accion':'Nuevo'}
    
class editar_detalle_compras(UpdateView):
    model=Detalle_compra
    fields='__all__'
    success_url=reverse_lazy('list_detalle_compras')
    extra_context={'accion':'Modificar'}

class eliminar_detalle_compras(DeleteView):
    model=Detalle_compra
    success_url=reverse_lazy('list_detalle_compras')
    extra_context={'accion':'Eliminar'}

#compra

class Lista_compras(ListView):
    model=Compra

class nuevo_compras(CreateView):
    model=Compra
    form_class=Form_compra
    success_url=reverse_lazy('list_compras')
    extra_context={'accion':'Nueva'}
    
class editar_compras(UpdateView):
    model=Compra
    fields='__all__'
    success_url=reverse_lazy('list_compras')
    extra_context={'accion':'Modificar'}

class eliminar_compras(DeleteView):
    model=Compra
    success_url=reverse_lazy('list_compras')
    extra_context={'accion':'Eliminar'}

#proveedores

class Lista_proveedores(ListView):
    model=Proveedor

class nuevo_proveedores(CreateView):
    model=Proveedor
    form_class=Form_proveedor
    success_url=reverse_lazy('list_proveedores')
    extra_context={'accion':'Nuevo'}
    
class editar_proveedores(UpdateView):
    model=Proveedor
    fields='__all__'
    success_url=reverse_lazy('list_proveedores')
    extra_context={'accion':'Modificar'}

class eliminar_proveedores(DeleteView):
    model=Proveedor
    success_url=reverse_lazy('list_proveedores')
    extra_context={'accion':'Eliminar'}

#articulo

class Lista_articulos(ListView):
    model=Articulo

class nuevo_articulos(CreateView):
    model=Articulo
    form_class=Form_articulo
    success_url=reverse_lazy('list_articulos')
    extra_context={'accion':'Nuevo'}
    
class editar_articulos(UpdateView):
    model=Articulo
    fields='__all__'
    success_url=reverse_lazy('list_articulos')
    extra_context={'accion':'Modificar'}

class eliminar_articulos(DeleteView):
    model=Articulo
    success_url=reverse_lazy('list_articulos')
    extra_context={'accion':'Eliminar'}

#Marca

class Lista_marcas(ListView):
    model=Marca

class nuevo_marcas(CreateView):
    model=Marca
    form_class=Form_marca
    success_url=reverse_lazy('list_marcas')
    extra_context={'accion':'Nueva'}
    
class editar_marcas(UpdateView):
    model=Marca
    fields='__all__'
    success_url=reverse_lazy('list_marcas')
    extra_context={'accion':'Modificar'}

class eliminar_marcas(DeleteView):
    model=Marca
    success_url=reverse_lazy('list_marcas')
    extra_context={'accion':'Eliminar'}