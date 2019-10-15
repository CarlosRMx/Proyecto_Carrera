from django.contrib import admin
from .models import Evaluacion_Medica
# Register your models here.



class Evaluacion_MedicaAdmin(admin.ModelAdmin):
    '''Admin View for Evaluacion_Medica'''

    list_display = ('nino','proxima_cita',)
    list_filter = ('proxima_cita',)
    search_fields = ('nino',)
    
admin.site.register(Evaluacion_Medica,Evaluacion_MedicaAdmin)