from django.urls import path
from articulos import views

urlpatterns = [
    path('',views.lista_articulos,name='lista_articulos'),
    path('nuevo',views.nuevo_articulos,name='nuevo_articulos'),
    path('eliminar/<int:id>',views.eliminar_articulos,name='eliminar_articulos'),
    path('editar/<int:id>',views.editar_articulos,name='editar_articulos'),
]
