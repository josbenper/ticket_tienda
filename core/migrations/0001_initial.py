# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('idArticulo', models.IntegerField(blank=True, max_length=35)),
                ('nombre', models.CharField(max_length=35)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.PositiveSmallIntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='LineaPedidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('idLineaPedido', models.CharField(blank=True, max_length=35)),
                ('cantidad', models.CharField(max_length=35)),
                ('precioTotalLinea', models.DecimalField(decimal_places=2, blank=True, max_digits=10)),
                ('articulo', models.OneToOneField(to='core.Articulos')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('idPedido', models.CharField(blank=True, max_length=35)),
                ('fecha', models.CharField(max_length=35)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lineapedidos',
            name='pedido',
            field=models.OneToOneField(to='core.Pedidos'),
        ),
    ]
