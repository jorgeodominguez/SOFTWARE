# Generated by Django 5.0.2 on 2024-06-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detalle_compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='rin',
            field=models.IntegerField(verbose_name='Rin'),
        ),
        migrations.AlterField(
            model_name='detalle_compra',
            name='observacion',
            field=models.TextField(default='nada', max_length=100, verbose_name='Observacion'),
        ),
    ]