from rest_framework.serializers import ModelSerializer
from ..models.Tipo_Insumo import Tipo_Insumo

class TipoInsumoSerializer(ModelSerializer):
    class Meta:
        model = Tipo_Insumo
        fields = '__all__'