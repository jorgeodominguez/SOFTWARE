from django.urls import path
from comisiones import views

urlpatterns = [
    path('', views.lista_comisiones),
]
