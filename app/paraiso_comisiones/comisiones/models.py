from django.db import models


class Comisiones(models.Model):
    empleado=models.ForeignKey("comisiones.empleados",verbose_name="Empleados",on_delete=models.DO_NOTHING)
    fecha=models.DateField('Fecha')
    pedido=models.CharField('Numero de Pedido',max_length=10)
    comision=models.DecimalField('Cantidad de Comision',max_digits=5,decimal_places=2)

    def __str__(self):
        return self.nombre

class Empleados(models.Model):
    nombre=models.CharField("Nombre",max_length=50)
    telefono=models.CharField('Telefono',max_length=12,null=True,blank=True)
    fecha_ingreso=models.DateField("Fecha de Ingreso")

    def __str__(self):
        return self.nombre