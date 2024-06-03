from django.db import models # type: ignore

class Detalle_compra(models.Model):
    compra=models.ForeignKey("detalle_compras.Compra",verbose_name="Compra",on_delete=models.DO_NOTHING)
    articulo=models.ForeignKey("detalle_compras.Articulo",verbose_name="Articulo",on_delete=models.DO_NOTHING)
    cantidad=models.IntegerField("Cantidad",null=False)
    validacion=models.IntegerField("Validacion",default=0)
    costo=models.DecimalField('Costo',max_digits=7,decimal_places=2)
    fecha=models.DateField("Fecha de Validacion")
    observacion=models.TextField('Observacion',max_length=100,default='nada')

    def __str__(self):
        return self.observacion

class Compra(models.Model):
    proveedor=models.ForeignKey("detalle_compras.Proveedor",verbose_name="Proveedor",on_delete=models.DO_NOTHING)
    folio=models.CharField('Folio',max_length=20,null=False)
    fecha=models.DateField("Fecha")
    total=models.DecimalField('Total',max_digits=7,decimal_places=2)

    def __str__(self):
        return self.folio

class Proveedor(models.Model):
    numero=models.IntegerField("Numero",null=False)
    nombre=models.CharField("Nombre",max_length=50,null=False)
    rfc=models.CharField("RFC",max_length=13,null=False)
    direccion=models.TextField("Direccion",max_length=100)
    cp=models.IntegerField("CP")
    estado=models.CharField("Estado",max_length=25)
    municipio=models.CharField("Municipio",max_length=25)
    telefono=models.CharField("Telefono",max_length=20)

    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    medida=models.CharField("Medida",max_length=20,null=False)
    clave=models.CharField('Clave',max_length=20,null=False)
    rin=models.IntegerField("Rin",null=False)
    marca=models.ForeignKey("detalle_compras.Marca",verbose_name="Marca",on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.medida
    
class Marca(models.Model):
    marca=models.CharField("Marca",max_length=50,null=False)
    disenio=models.CharField('Diseño',max_length=50,null=False)

    def __str__(self):
        return self.marca
