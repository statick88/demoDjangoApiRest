from django.db import models

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    web = models.URLField()
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
