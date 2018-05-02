from rest_framework import serializers
from .models import Articulos, Pedidos, LineaPedidos
from django.contrib.auth.models import User

class ArticulosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articulos
        fields = ('idArticulo', 'nombre', 'precio')

class ArticuloLineaPedido(serializers.ModelSerializer):

    class Meta:
        model = Articulos
        fields = ('nombre', 'precio')

class PedidosSerializer(serializers.ModelSerializer):

    #User = serializers.StringRelatedField(many=True)

    class Meta:
        model = Pedidos
        fields = ('idPedido', 'total')

class LineaPedidosSerializer(serializers.ModelSerializer):

    articulo = ArticuloLineaPedido()
    pedido = PedidosSerializer()
    #User = serializers.StringRelatedField(many=True)

    class Meta:
        model = LineaPedidos
        fields = ('pedido', 'idLineaPedido', 'articulo', 'cantidad', 'precioTotalLinea')

