from django.contrib import admin
from .models import Noticia
from django.utils.safestring import mark_safe
# Register your models here.


class NoticiaAdmin(admin.ModelAdmin):
    '''Admin View for Noticia'''

    list_display = ('titulo_noticia','fecha_publicacion','Imagen',)
    list_filter = ('fecha_publicacion',)
    search_fields = ('titulo_noticia',)
    readonly_fields = ("Imagen",)
    def Imagen(self, obj):
        return mark_safe(
            '<img src="{url}" style="max-width: 100px"/>'.format(url=obj.imagen.url)
        )

admin.site.register(Noticia,NoticiaAdmin)