from django.db import models

# Create your models here.
class Logo(models.Model):
    description = models.CharField('Descripcion', max_length=32)
    image = models.ImageField('Imagen')
