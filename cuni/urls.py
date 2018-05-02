from django.conf.urls import url, include
from core import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/listado_articulos', views.ListArticulos),
#router.register(r'api/listado_pedidos', views.ListPedidos),
#router.register(r'api/listado_linea_pedidos', views.ListLineaPedidos),





# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/pedidosCSV', views.PedidosCSV.as_view(), name='csv')
    url(r'^api/pedidosEmail', views.PedidosEmail.as_view(), name='email')
]
