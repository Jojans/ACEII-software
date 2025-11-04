from django.db import models

from django.utils import timezone

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)  # Código único para identificar el producto
    codigo_barras = models.CharField(max_length=50, unique=True, blank=True, null=True)  # Código de barras opcional
    nombre = models.CharField(max_length=255, unique=True)  # Nombre único del producto
    precio_interno = models.DecimalField(max_digits=10, decimal_places=2)  # Precio interno
    precio_publico = models.DecimalField(max_digits=10, decimal_places=2)  # Precio de venta al público

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    

class Venta(models.Model):
    fecha = models.DateField()  # Guarda solo el día, mes y año
    caja_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_dia = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    # Cambiar a CharField para permitir guardar los datos como cadenas de texto separadas por comas
    cantidad = models.CharField(max_length=255, default='')  # Cantidades concatenadas
    precio = models.CharField(max_length=255, default='')  # Precios concatenados
    total_producto = models.CharField(max_length=255, default='')  # Totales concatenados
    producto = models.CharField(max_length=255, default='')  # Productos concatenados

    def __str__(self):
        return f"Venta {self.id} - {self.fecha}"

    def calcular_total(self):
        """Calcula el total de la venta (sumando todos los productos y cantidades)"""
        total = 0
        # Aquí podrías considerar dividir las cadenas para obtener los totales si lo necesitas
        totales = self.total_producto.split(',')
        for total_producto in totales:
            total += float(total_producto)  # Sumar los totales de los productos
        return total + self.caja_inicial