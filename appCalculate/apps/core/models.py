from django.db import models

# Create your models here.
class Persona(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=32, blank=False, null=False)
    last_name = models.CharField(verbose_name='Apellido', max_length=32) # blanck y null por defecto son False

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self) -> str:
        return f"<Persona: {self.name} {self.last_name}>"
