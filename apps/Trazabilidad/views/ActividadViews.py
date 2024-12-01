from rest_framework.viewsets import ModelViewSet
from ..models.Actividad import Actividad
from ..serializers.ActividadSerializer import ActividadSerializer

class ActividadViews(ModelViewSet):
    queryset = Actividad.objects.all()
    fields = '__all__'