from django.db import models

# Create your models here.
class Logo(models.Model):
    description = models.CharField('Descripcion', max_length=32)
    image = models.ImageField('Imagen')

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logotipos"

    def __str__(self) -> str:
        return f'Descripción: {self.description}' 

    


