from django.contrib import admin
from .models import Producto,Categoria_Producto
from django.utils.safestring import mark_safe
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    '''Admin View for Producto'''

    list_display = ('nombre_producto','unidades','fecha_vencimiento','Imagen_producto',)
    list_filter = ('fecha_vencimiento',)
    search_fields = ('nombre_producto',)
    readonly_fields = ("Imagen_producto",)
    def Imagen_producto(self, obj):
        return mark_safe(
            '<img src="{url}" style="max-width: 100px"/>'.format(url=obj.image.url)
        )

class Categoria_ProductoAdmin(admin.ModelAdmin):
    '''Admin View for Categoria_Producto'''

    list_display = ('nombre_categoria','estado',)
    search_fields = ('nombre_categoria',)
    
    
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria_Producto,Categoria_ProductoAdmin)
