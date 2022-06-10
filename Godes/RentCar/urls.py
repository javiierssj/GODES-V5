from django.urls import path
from .views import inicio, info, perfil, ordenes, registro, registro_auto, inicioSesion

urlpatterns = {
    path('',inicio,name="inicio"),
    path('informacion/',info,name="info"),
    path('perfil/',perfil,name="perfil"),
    path('ordenes/',ordenes,name="ordenes"),
    path('registro/',registro,name="registro"),
    path('registro_auto/',registro_auto,name="registro_auto"),
    path('inicioSesion/',inicioSesion,name="inicioSesion"),
 }