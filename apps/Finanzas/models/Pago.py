from django.db import models
from apps.Trazabilidad.models.Asignacion_actividad import Asignacion_actividad

class Pago(models.Model):
    fk_asignacion_actividad = models.ForeignKey(Asignacion_actividad,on_delete=models.SET_NULL,null=True)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    def __str__(self):
        return self.fecha