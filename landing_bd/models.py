from django.db import models
from django.contrib.auth.models import User
from.listas_de_modelos import RELEVANCIA_CHOICES, SITUACION_CHOICES

class Familia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre

class Sociedades(models.Model):
    nombre = models.CharField( max_length=50, unique=True)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='sociedades_familia')
    
    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    ejecutivo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clientes_ejecutivos')
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='clientes_familia')
    direcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=False)
    relevancia = models.CharField(choices=RELEVANCIA_CHOICES, max_length=20, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
  
class Reuniones(models.Model):
    titulo = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=False, auto_now_add=False, default="0000-00-00")
    situacion = models.CharField(max_length=20, choices=SITUACION_CHOICES, null=True)
    ejecutivo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reunion_ejecutivo')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reunion_cliente')
    comentario = models.TextField(null=True)
    archivo = models.FileField(null=True, blank=True, upload_to='media/archivos/')
    
    def __str__(self):
        return f'{self.titulo} {self.cliente} / {self.fecha}'
    