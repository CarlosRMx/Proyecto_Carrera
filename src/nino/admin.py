from django.contrib import admin
from .models import NNA,Area_Dental,Area_Medica,Area_Psicologica,Area_Social,Idioma,Enfermedad,Etnia,Motivo_Ingreso,Fuente_Estre,Nivel_Nutricion,Relacion_Familia
from django.utils.safestring import mark_safe

# Register your models here.

class NNAAdmin(admin.ModelAdmin):
    '''Admin View for NNA'''

    list_display = ('nombre_nino','apellido_nino','sexo','motivo_ingreso','fecha_nacimiento','cui','Fotografia',)
    list_filter = ('fecha_evaluacion','motivo_ingreso',)
    search_fields = ('nombre_nino','apellido_nino','cui',)
    readonly_fields = ("Fotografia",)
    def Fotografia(self, obj):
        return mark_safe(
            '<img src="{url}" style="max-width: 100px"/>'.format(url=obj.image.url)
        )

class Area_DentalAdmin(admin.ModelAdmin):
    '''Admin View for Area_Dental'''

    list_display = ('nino','proxima_cita','diagnostico',)
    list_filter = ('proxima_cita',)
    search_fields = ('diagnostico',)

class Area_MedicaAdmin(admin.ModelAdmin):
    '''Admin View for Area_Medica'''

    list_display = ('nino','peso','altura','nivel_nutricion',)
    

class Area_SocialAdmin(admin.ModelAdmin):
    '''Admin View for Area_Social'''

    list_display = ('nino','relacion_familiar','fuente_estres','visitas_autorizadas',)

class Area_PsicologicaAdmin(admin.ModelAdmin):
    '''Admin View for Area_Psicologica'''

    list_display = ('nino','estado_emocional','percepcion_calidad_vida','enfermedad',)
    
class IdiomaAdmin(admin.ModelAdmin):
    '''Admin View for Idioma'''

    list_display = ('nombre_idioma','estado',)
    search_fields = ('nombre_idioma',)

class Motivo_IngresoAdmin(admin.ModelAdmin):
    '''Admin View for Motivo_Ingreso'''

    list_display = ('nombre_motivo','estado',)
    search_fields = ('nombre_motivo',)

class EnfermedadAdmin(admin.ModelAdmin):
    '''Admin View for Enfermedad'''

    list_display = ('nombre_enfermedad','estado',)
    search_fields = ('nombre_enfermedad',)


class EtniaAdmin(admin.ModelAdmin):
    '''Admin View for Etnia'''

    list_display = ('nombre_etnia','estado',)

class Fuente_EstreAdmin(admin.ModelAdmin):
    '''Admin View for Fuente_Estre'''

    list_display = ('nombre_fuente','estado',)
    
    
###########Paginas registradas en la administracion##########################
admin.site.site_header="CANICA"
admin.site.register(NNA,NNAAdmin)
admin.site.register(Area_Dental,Area_DentalAdmin)
admin.site.register(Area_Medica,Area_MedicaAdmin)
admin.site.register(Area_Psicologica,Area_PsicologicaAdmin)
admin.site.register(Area_Social,Area_SocialAdmin)
admin.site.register(Enfermedad,EnfermedadAdmin)
admin.site.register(Etnia,EtniaAdmin)
admin.site.register(Motivo_Ingreso,Motivo_IngresoAdmin)
admin.site.register(Nivel_Nutricion)
admin.site.register(Fuente_Estre,Fuente_EstreAdmin)
admin.site.register(Relacion_Familia)
admin.site.register(Idioma,IdiomaAdmin)