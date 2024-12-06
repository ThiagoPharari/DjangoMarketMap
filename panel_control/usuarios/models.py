from django.db import models

class Admin(models.Model):
    nombre = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Usuario(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellido = models.CharField(max_length=255, null=True, blank=True)
    correo = models.EmailField(max_length=255, null=True, blank=True)
    dni = models.CharField(max_length=255, unique=True, null=True, blank=True)
    numero = models.CharField(max_length=255, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=[('activo'), ('baneado')], default='activo')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
