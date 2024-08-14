from django.db import models
from apps.materials.models import Materials


class Items(models.Model):
    material = models.ForeignKey(Materials, on_delete=models.CASCADE)
    area = models.FloatField()
    thickness = models.FloatField()

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        unique_together = ['material']

    def __str__(self) -> str:
        return f"<Material: {self.material.name} - {self.area} - {self.thickness}>"


class CalculateList(models.Model):
    materials = models.ManyToManyField(Items, related_name='calculate_lists')

    class Meta:
        verbose_name = "Lista de Materiales"
        verbose_name_plural = "Lista de Materiales"

    def __str__(self) -> str:
        return f"<Materiales: {self.materials}>"