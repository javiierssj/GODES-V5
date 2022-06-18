from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'RentCar/main_page.html')

def informacion(request):
    return render(request, 'RentCar/Pag_info.html')

def perfil(request):
    return render(request, 'RentCar/pagina_perfil.html')

def ordenes(request):
    return render(request, 'RentCar/pag_registro.html')

def registro(request):
    return render(request, 'RentCar/pag_formulario.html')

def registro_auto(request):
    return render(request, 'RentCar/pag_form_auto.html')

def inicioSesion(request):
    return render(request, 'RentCar/InicioSesion.html')

