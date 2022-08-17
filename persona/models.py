from django.db import models

# Create your models here.
class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)