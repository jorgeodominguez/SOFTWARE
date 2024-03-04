from django.shortcuts import render
from comisiones.models import Comisiones

def lista_comisiones(request):
    comisiones=Comisiones.objects.all()

    return render(request,'comisiones.html',{'comisiones':comisiones})

