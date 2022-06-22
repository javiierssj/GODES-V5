from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from RentCar.models import vehiculo, usuario, marca
from .serializers import vehiculoSerializer, usuarioSerializer, marcaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_vehiculo(request):
    if request.method == 'GET':
        vehiculo1 = vehiculo.objects.all()
        serializer = vehiculoSerializer(vehiculo1,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = vehiculoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarvehiculo(request,pat):
    try:
        m = vehiculo.objects.get(patente = pat)
    except vehiculo.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = vehiculoSerializer(m, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_usuarios(request):
    if request.method == 'GET':
        usuario1 = usuario.objects.all()
        serializer = usuarioSerializer(usuario1,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = usuarioSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarUsuario(request,run):
    try:
        m = usuario.objects.get(rut_o_pasaporte = run)
    except usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = usuarioSerializer(m, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_marca(request):
    if request.method == 'GET':
        marca1 = marca.objects.all()
        serializer = marcaSerializer(marca1,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = marcaSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarMarca(request,marcaId):
    try:
        m = marca.objects.get(id_marca = marcaId)
    except marca.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = marcaSerializer(m, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)