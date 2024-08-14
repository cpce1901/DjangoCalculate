from django.db import models

   
class Materials(models.Model):
    name = models.CharField('Nombre', max_length=64)
    density = models.IntegerField('Densidad kg/m3')
    co2_factor = models.IntegerField('FE Kg/co2')
    thermic_trans = models.FloatField('Transmitancia térmica')
    
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

    def __rpr__(self) -> str:
        return f"<Material: {self.name} - {self.density} - {self.co2_factor} - {self.thermic_trans}>"
    
    def __str__(self) -> str:
        return f"{self.name.upper()}"
    


