# Generated by Django 5.0.2 on 2024-02-26 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensaje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
    ]
