# Generated by Django 2.0.13 on 2019-10-14 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=30, verbose_name='Nombre de la categoria')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Categoria_Producto',
                'verbose_name_plural': 'Categoria_Productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30, verbose_name='Nombre del producto')),
                ('image', models.ImageField(upload_to='img', verbose_name='Imagen del producto')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('fecha_ingreso', models.DateField(auto_now_add=True, verbose_name='Fecha de ingreso a bodega')),
                ('unidades', models.IntegerField(verbose_name='Unidades')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de vencimiento')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.AddField(
            model_name='categoria_producto',
            name='producto',
            field=models.ManyToManyField(to='inventario.Producto'),
        ),
    ]
