from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Categorías"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['-fecha_creacion']

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    
    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"
    
    class Meta:
        ordering = ['-fecha']

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"

class Slide(models.Model):
    titulo = models.CharField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to='slides/')
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Slide {self.orden} - {self.titulo}"
    
    class Meta:
        ordering = ['orden']

class ConfiguracionSitio(models.Model):
    mensaje_envio = models.CharField(max_length=200, default='Envíos a domicilio en 3 días hábiles')
    activo = models.BooleanField(default=True)
    
    # Colores del sitio
    color_primario = models.CharField(max_length=7, default='#495057', help_text='Color principal (botones, enlaces)')
    color_secundario = models.CharField(max_length=7, default='#6c757d', help_text='Color secundario (texto, bordes)')
    color_fondo = models.CharField(max_length=7, default='#f8f9fa', help_text='Color de fondo del sitio')
    color_banner = models.CharField(max_length=7, default='#28a745', help_text='Color del banner de envío')
    color_cards = models.CharField(max_length=7, default='#ffffff', help_text='Color de fondo de las cards')
    color_hover = models.CharField(max_length=7, default='#F4C2C2', help_text='Color de hover en navegación')
    
    def __str__(self):
        return "Configuración del Sitio"
    
    class Meta:
        verbose_name = "Configuración del Sitio"
        verbose_name_plural = "Configuración del Sitio"