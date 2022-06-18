from django.urls import path
from .views import inicio, informacion, perfil, ordenes, registro, registro_auto, inicioSesion

urlpatterns = {
    path('',inicio,name="inicio"),
    path('informacion/',informacion,name="informacion"),
    path('perfil/',perfil,name="perfil"),
    path('ordenes/',ordenes,name="ordenes"),
    path('registro/',registro,name="registro"),
    path('registro_auto/',registro_auto,name="registro_auto"),
    path('inicioSesion/',inicioSesion,name="inicioSesion"),
 }