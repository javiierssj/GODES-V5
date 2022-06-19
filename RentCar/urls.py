from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .views import inicio, informacion, perfil, ordenes, registro, registro_auto, registarauto, inicioSesion, registrarusuario, login_view ,logout_view, catalogo_planilla, info_auto, mod_auto


urlpatterns = [
    path('',inicio,name="inicio"),
    path('informacion/',informacion,name="informacion"),
    path('perfil/',perfil,name="perfil"),
    path('ordenes/',ordenes,name="ordenes"),
    path('registro/',registro,name="registro"),
    path('registro_auto/',registro_auto,name="registro_auto"),
    path('mod_auto/<pat>', mod_auto,name="mod_auto"),
    path('registarauto/',registarauto,name="registarauto"),
    path('inicioSesion/',inicioSesion,name="inicioSesion"),
    path('registrarusuario', registrarusuario, name="registrarusuario"),
    path('catalogo_planilla/',catalogo_planilla,name="catalogo_planilla"),
    path('catalogo_planilla/<pat>', info_auto,name="info_auto"),

    path('acceso/',LoginView.as_view(template_name='RentCar/InicioSesion.html'),name="acceso"),
    path('sesion',login_view,name="sesion"),
    path('inicio',logout_view,name="logout"),
 ]