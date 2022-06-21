from rest_framework import serializers
from RentCar.models import vehiculo, usuario

class vehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = '__all__'

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'