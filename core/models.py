from django.db import models
from django.contrib.auth.models import User

# Modelo Articulos.
class Articulos(models.Model):
	idArticulo = models.IntegerField(max_length=35, blank=True)
	nombre = models.CharField(max_length=35)
	precio = models.DecimalField(max_digits=6, decimal_places=2)
	stock = models.PositiveSmallIntegerField(default='0')

	def save(self, *args, **kwargs):
		if not self.idArticulo:
			i = Articulos.objects.all().order_by('-idArticulo')[0]
			self.idArticulo = i.idArticulo+1
		super(Articulos, self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre

"""
# Modelo Usuarios.
class Articulos(models.Model):
	idUsuario = models.CharField(max_length=35)
	nombre = models.CharField(max_length=35)
	apellidos = models.CharField(max_length=35)
	nombre_usuario = models.CharField(max_length=35)
	contrasena = models.CharField(max_length=35)

	def save(self, *args, **kwargs):
		if not self.idUsuario:
			i = Articulos.objects.all().order_by('-idUsuario')[0]
			self.idUsuario = i.idUsuario+1
		super(Articulos, self).save(*args, **kwargs)

	def __str__(self):
		return self.nombre

"""

# Modelo Pedidos.
class Pedidos(models.Model):
	idPedido = models.IntegerField(max_length=35, blank=True)
	#fecha = models.CharField(max_length=35)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	total = models.IntegerField(max_length=35, blank=True, default=0)

	def save(self, *args, **kwargs):
		if not self.idPedido:
			i = Pedidos.objects.all().order_by('-idPedido')[0]
			self.idPedido = i.idPedido+1
		super(Pedidos, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.total)

# Modelo LineaPedidos.
class LineaPedidos(models.Model):
	idLineaPedido = models.IntegerField(max_length=35, blank=True)
	pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
	articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
	cantidad = models.IntegerField(max_length=35)
	precioTotalLinea = models.IntegerField(max_length=35, blank=True)

	def save(self, *args, **kwargs):
		if not self.idLineaPedido:
			i = LineaPedidos.objects.all().order_by('-idLineaPedido')[0]
			self.idLineaPedido = i.idLineaPedido+1

		self.precioTotalLinea = int(self.cantidad) * int(self.articulo.precio)
		
		
		super(LineaPedidos, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.idLineaPedido)