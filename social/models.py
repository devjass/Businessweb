from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre de clave", max_length=100, unique=True)#Campo que permite solo texto alfanúmerico, guiones o barras, no permite carácteres especiales
    name = models.CharField(verbose_name="Red Social",max_length=200)
    url = models.URLField(verbose_name="Enlace",max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name

