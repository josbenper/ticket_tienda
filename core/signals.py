from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Articulos, Pedidos, LineaPedidos
import os.path
from django.conf import settings


@receiver(pre_save, sender=LineaPedidos)
def model_post_save(sender, instance, **kwargs):

	instance.pedido.total += instance.precioTotalLinea