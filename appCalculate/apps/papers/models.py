from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class Papers(models.Model):
    title = models.CharField('Título', max_length=256)
    author = models.CharField('Autor', max_length=256)
    details = models.TextField('Reseña', null=True, blank=True)
    reference = models.CharField('Referencia', max_length=512)
    imagen = models.ImageField('Imagen', upload_to='papers/img/', null=True, blank=True)
    file = models.FileField('Documento', upload_to='papers/file/', null=True, blank=True)


    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f"{self.title}"