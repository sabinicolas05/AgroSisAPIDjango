from rest_framework.serializers import ModelSerializer
from apps.Finanzas.models.Venta import *
from apps.Finanzas.models.Produccion import *
from ..models.Venta import Venta

class VentaSerializer(ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'


        

 class ProduccionSerializer(ModelSerializer):
     class Meta:
         model = Produccion
         fields = '__all__'




 class VentaSerializer(ModelSerializer):
     produccion = ProduccionSerializer()  
     class Meta:
         model = Venta
         fields = '__all__'