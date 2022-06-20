from django.urls import path
from rest_vehiculo.viewsLogin import ini_user
from rest_vehiculo.views import listado_vehiculo, modEliminarvehiculo

urlpatterns = [
    path('listado_vehiculo/', listado_vehiculo, name="listado_vehiculo"),
    path('modEliminarvehiculo/<pat>', modEliminarvehiculo, name="modEliminarvehiculo"),
    path('ini_user/', ini_user, name="ini_user"),
]