from rest_framework import serializers
from RentCar.models import vehiculo

class vehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = '__all__'