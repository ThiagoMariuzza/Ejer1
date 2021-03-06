# Generated by Django 2.2 on 2020-05-14 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=50)),
                ('Editorial', models.CharField(max_length=50)),
                ('Paginas', models.IntegerField()),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Localizacion', models.CharField(max_length=50)),
                ('Libro', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Libro')),
                ('Usuario', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Usuario')),
            ],
        ),
    ]
