from django.urls import reverse_lazy # type: ignore
from django.views.generic import ListView,TemplateView # type: ignore
from django.views.generic.edit import CreateView,UpdateView,DeleteView # type: ignore
from articulos.forms import FormCategoria
from articulos.models import Categoria
#from django.contrib.messages.views import SuccessMessageMixin
#from django.contrib import messages

class ListaCategorias(ListView):
    model=Categoria

class nuevaCategoriaView(CreateView):
    model=Categoria
    form_class=FormCategoria
    success_url=reverse_lazy('categorias_list')
    extra_context={'accion':'Nueva'}
    

class editarCategoriaView(UpdateView):
    model=Categoria
    fields='__all__'
    success_url=reverse_lazy('categorias_list')
    extra_context={'accion':'Modificar'}

class eliminarCategoriaView(DeleteView):
    model=Categoria
    success_url=reverse_lazy('categorias_list')
    extra_context={'accion':'Eliminar'}

class BienvenidaView(TemplateView):
    template_name='bienvenida.html'