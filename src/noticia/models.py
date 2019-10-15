from django.db import models
from django import forms
# Create your models here.
class Noticia(models.Model):
    """Model definition for Noticia."""

    # TODO: Define fields here
    titulo_noticia=models.CharField(max_length=40,verbose_name="Título de la noticia")
    imagen=models.ImageField(upload_to="img",verbose_name="Fotografía de la notica")
    fecha_publicacion=models.DateField(auto_now_add=True,verbose_name="Fecha de publicación")
    descripcion=models.TextField(verbose_name="Descripción")


    class Meta:
        """Meta definition for Noticia."""

        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo_noticia+" "+str(self.fecha_publicacion)
    
    def get_absolute_url(self):
        return u'/noticia/%d' % self.id 