from django.db import models

# Create your models here.
class Papers(models.Model):
    title = models.CharField('Título', max_length=256)
    author = models.CharField('Autor', max_length=64)
    description = models.TextField('Cuerpo')
    reference = models.CharField('Referencia', max_length=512)
    imagen = models.ImageField('Imagen', upload_to='papers/img/', null=True, blank=True)
    file = models.FileField('Documento', upload_to='papers/file/', null=True, blank=True)


    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"


    def __str__(self) -> str:
        return f"{self.title}"