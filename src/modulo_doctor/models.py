from django.db import models
from nino.models import NNA
# Create your models here.

class Evaluacion_Medica(models.Model):
    """Model definition for Evaluacion_Medica."""

    # TODO: Define fields here
    nino=models.ForeignKey(NNA,on_delete=models.CASCADE)
    DESNUTRICION=[
        ("S","Si"),
        ("N","No")
    ]
    edad=models.IntegerField(verbose_name="Edad del niño")
    peso=models.IntegerField(verbose_name="Peso del niño")
    desnutricion=models.CharField(max_length=3,choices=DESNUTRICION,verbose_name="Desnutrición")
    altura=models.FloatField(verbose_name="Altura del niño")
    circunferencia_brazo_derecho=models.FloatField(verbose_name="Circunferencia del brazo derecho")
    circunferencia_brazo_izquierdo=models.FloatField(verbose_name="Circunferencia del brazo izquierdo")
    circunferencia_abdominal=models.FloatField(verbose_name="Circunferencia abdominal")
    imc=models.FloatField(verbose_name="I.M.C (Indice de masa corporal)")
    antecendentes_medicos=models.TextField("Antecedentes médicos de importancia")
    padece_alergias=models.CharField(max_length=30,verbose_name="Padece de alegias, cual",null=True,blank=True)
    sintomas=models.TextField(verbose_name="Sintomas",null=True,blank=True)
    impresion_clinica=models.TextField(verbose_name="Impresión clínica")
    recomendacion=models.TextField(verbose_name="Recomendaciones",null=True,blank=True)
    tratamiento=models.TextField(verbose_name="Tratamiento",null=True,blank=True)
    proxima_cita=models.DateField(verbose_name="Próxima cita")
    observaciones=models.TextField(verbose_name="Observaciones",null=True,blank=True)

    class Meta:
        """Meta definition for Evaluacion_Medica."""

        verbose_name = 'Evaluacion_Medica'
        verbose_name_plural = 'Evaluacion_Medicas'

    def __str__(self):
        return str(self.nino)