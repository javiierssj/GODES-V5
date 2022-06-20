from rest_framework import serializers
from RentCar.models import vehiculo

class vehiculoSerializers(serializers.ModelSerializers)
    class Meta:
        model = vehiculo
        field = ¨['patente','nro_chasis','color','rendimiento']