from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .views import inicio, informacion, mod_perfil, ordenes, registro, registarauto, inicioSesion, registrarusuario, login_view ,logout_view, catalogo_planilla, info_auto, mod_auto, eliminarAuto, perfil, registraOrdenV2, registraOrden, eliminarOrden


urlpatterns = [
    path('',inicio,name="inicio"),
    path('informacion/',informacion,name="informacion"),
    path('perfil',login_required(perfil),name="perfil"),
    path('mod_perfil/<id>/',mod_perfil,name="mod_perfil"),
    path('ordenes/',login_required(ordenes),name="ordenes"),
    path('registro/',registro,name="registro"),
    path('mod_auto/<pat>', login_required(mod_auto),name="mod_auto"),
    path('registarauto/',login_required(registarauto),name="registarauto"),
    path('eliminarAuto/<pat>',eliminarAuto,name="eliminarAuto"),
    path('inicioSesion/',inicioSesion,name="inicioSesion"),
    path('registrarusuario', registrarusuario, name="registrarusuario"),
    path('catalogo_planilla/',catalogo_planilla,name="catalogo_planilla"),
    path('catalogo_planilla/<pat>', info_auto,name="info_auto"),
    path('registraOrdenV2', login_required(registraOrdenV2), name="registraOrdenV2"),
    path('add-orden/', registraOrden, name="registraOrden"),
    path('eliminarOrden/<id>', eliminarOrden, name="eliminarOrden"),

    path('acceso/',LoginView.as_view(template_name='RentCar/InicioSesion.html'),name="acceso"),
    path('sesion',login_view,name="sesion"),
    path('inicio',logout_view,name="logout"),
 ]