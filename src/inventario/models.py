from django.db import models

# Create your models here.

class Producto(models.Model):
    """Model definition for Producto."""

    # TODO: Define fields 
    nombre_producto=models.CharField(max_length=30,verbose_name="Nombre del producto")
    image=models.ImageField(upload_to="img",verbose_name="Imagen del producto")
    descripcion=models.TextField(verbose_name="Descripcion")
    fecha_ingreso=models.DateField(auto_now_add=True,verbose_name="Fecha de ingreso a bodega")
    unidades=models.IntegerField(verbose_name='Unidades')
    fecha_vencimiento=models.DateField(verbose_name="Fecha de vencimiento")
    estado=models.BooleanField(default=True,verbose_name="Estado")

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre_producto
    
    def get_absolute_url(self):
        return u'/inventario/%d' % self.id 

class Categoria_Producto(models.Model):
    """Model definition for Categoria_Producto."""

    # TODO: Define fields here
    nombre_categoria=models.CharField(max_length=30,verbose_name="Nombre de la categoria")
    descripcion=models.TextField(verbose_name="Descripción")
    producto=models.ManyToManyField(Producto)
    estado=models.BooleanField(default=True,verbose_name="Estado")

    class Meta:
        """Meta definition for Categoria_Producto."""

        verbose_name = 'Categoria_Producto'
        verbose_name_plural = 'Categoria_Productos'

    def __str__(self):
        return self.nombre_categoria

