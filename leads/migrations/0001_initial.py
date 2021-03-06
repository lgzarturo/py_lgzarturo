# Generated by Django 2.2.5 on 2019-09-29 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre del prospecto')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('website', models.URLField(blank=True, verbose_name='Sitio web')),
                ('phone', models.CharField(blank=True, max_length=32, verbose_name='Teléfono')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('source', models.CharField(blank=True, max_length=64, null=True, verbose_name='Fuente')),
                ('medium', models.CharField(blank=True, max_length=64, null=True, verbose_name='Medio')),
                ('campaign', models.CharField(blank=True, max_length=64, null=True, verbose_name='Campaña')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
            ],
            options={
                'verbose_name': 'Prospecto',
                'verbose_name_plural': 'Prospectos',
            },
        ),
    ]
