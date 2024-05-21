# Generated by Django 5.0.2 on 2024-05-21 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medida', models.CharField(max_length=20, verbose_name='Medida')),
                ('clave', models.CharField(max_length=20, verbose_name='Clave')),
                ('rin', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Rin')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(max_length=20, verbose_name='Folio')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('total', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('disenio', models.CharField(max_length=50, verbose_name='Diseño')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('rfc', models.CharField(max_length=13, verbose_name='RFC')),
                ('direccion', models.TextField(max_length=100, verbose_name='Direccion')),
                ('cp', models.IntegerField(verbose_name='CP')),
                ('estado', models.CharField(max_length=25, verbose_name='Estado')),
                ('municipio', models.CharField(max_length=25, verbose_name='Municipio')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telfono')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('validacion', models.IntegerField(default=0, verbose_name='Validacion')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Costo')),
                ('fecha', models.DateField(verbose_name='Fecha de Validacion')),
                ('observacion', models.TextField(max_length=100, verbose_name='Observacion')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='detalle_compras.articulo', verbose_name='Articulo')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='detalle_compras.compra', verbose_name='Compra')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='detalle_compras.marca', verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='detalle_compras.proveedor', verbose_name='Proveedor'),
        ),
    ]
