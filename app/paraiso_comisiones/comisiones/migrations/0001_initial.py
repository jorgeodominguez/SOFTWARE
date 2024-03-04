# Generated by Django 5.0.2 on 2024-03-04 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('telefono', models.CharField(blank=True, max_length=12, null=True, verbose_name='Telefono')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de Ingreso')),
            ],
        ),
        migrations.CreateModel(
            name='Comisiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('pedido', models.CharField(max_length=10, verbose_name='Numero de Pedido')),
                ('comision', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cantidad de Comision')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='comisiones.empleados', verbose_name='Empleados')),
            ],
        ),
    ]
