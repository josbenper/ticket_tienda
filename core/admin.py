from django.contrib import admin
from .models import Articulos, Pedidos, LineaPedidos

admin.site.register(Articulos)
admin.site.register(Pedidos)
admin.site.register(LineaPedidos)

