from rest_framework import serializers
from RentCar.models import vehiculo, usuario, marca

class vehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = '__all__'

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'

class marcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = marca
        fields = '__all__'