from django.shortcuts import render
from .models import Articulos, Pedidos, LineaPedidos
from core.serializer import ArticulosSerializer, PedidosSerializer, LineaPedidosSerializer
from rest_framework import viewsets
from rest_framework import generics
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.db.models import Count

from djqscsv import render_to_csv_response
from django.core.mail import send_mail


#Vista Articulos
class ListArticulos(viewsets.ModelViewSet):
    """
    Endpoint que muestran todos los Articulos.<p>
    introduciendo en la url el id del articulo se puede modificar/eliminar dicho articulo.<p>
    Ejemplo http://127.0.0.1:8000/api/listado_articulos/1
    """
    queryset = Articulos.objects.all()
    serializer_class = ArticulosSerializer

#Vista Pedidos
class ListPedidos(viewsets.ModelViewSet):
    """
    Endpoint que muestran todos los Pedidos.
    """
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer


#Vista Linea de pedidos
class ListLineaPedidos(viewsets.ModelViewSet):
    """
    Endpoint que muestran todas las lineas de pedidos.
    """
    queryset = LineaPedidos.objects.all()
    serializer_class = LineaPedidosSerializer

#vista CSV
class PedidosCSV(ListView):
    """
    API endpoint que genera un CSV con los pedidos del usuario citado

    Hay que enviar por la url el usuario para ver los pedidos del usuario:
        http://127.0.0.1:8000/api/pedidosCSV?user=Juan
    """
    def get(self, request, *args, **kwargs):
        
        userName = request.GET.get('user')
        queryset = Pedidos.objects.filter(usuario__username=userName)
        if queryset:

            queryset2 = LineaPedidos.objects.filter(pedido__idPedido=queryset.values('idPedido')).values('idLineaPedido')
            pedidos = queryset2.filter(pedido__idPedido=queryset.values('idPedido')).values('articulo__nombre', 'cantidad', 'precioTotalLinea', 'pedido__usuario__username')
            articulo = queryset2.filter(pedido__idPedido=queryset.values('idPedido')).values('articulo__nombre')

            #return HttpResponse(mensaje)
            return render_to_csv_response(pedidos)
            #message.attach_file('/api/pedidosCSV?user=Juan')
        else:
            return HttpResponse("El usuario " + userName + " no tiene ninguna compra.")


class PedidosEmail(ListView):
    def get(self, request, *args, **kwargs):
        userName = request.GET.get('user')
            queryset = Pedidos.objects.filter(usuario__username=userName)
            if queryset:
                queryset2 = LineaPedidos.objects.filter(pedido__idPedido=queryset.values('idPedido')).values('idLineaPedido')
                pedidos = queryset2.filter(pedido__idPedido=queryset.values('idPedido'))
                mensaje =  "El usuario " + userName + " ha pedido " + str(pedidos.values('articulo__nombre')) + " por un valor de " + str(pedidos.values('pedido__total')[:1])
               
                

                html_content = "Comment tu vas?"
                email = EmailMessage("my subject", html_content, "from@example.com", to@example.com])
                email.content_subtype = "html"
               
                email.attach_file('http://127.0.0.1:8000/api/pedidosCSV?user='+userName)

                res = email.send()
                return HttpResponse('%s'%res)

