from django.db import models

#CHOISES
GENERO=[
    ('1','Acción'),
    ('2','Aventura'),
    ('3','Carrera')
]


class Articulos(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField('Descripción',null=True,blank=True)
    stock=models.IntegerField(default=0)
    genero=models.CharField('Género',max_length=1,choices=GENERO)

    def __str__(self):
        return self.nombre