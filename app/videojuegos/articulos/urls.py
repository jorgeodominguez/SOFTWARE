from django.urls import path
from articulos import views

urlpatterns = [
    path('',views.lista_articulos,name='lista_articulos'),
    path('eliminar/<int:id>',views.eliminar_articulos,name='eliminar_articulos'),
]
