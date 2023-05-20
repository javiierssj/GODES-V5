from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from .models import usuario, vehiculo, modelo, status, orden
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import vehiculoForm, usuarioForm



# Create your views here.

def registrarusuario(request):
    rutUsuario_u = request.POST['rut']
    nomUsuario_u  = request.POST['nombreu']
    conUsuario_u  = request.POST['clave']
    apellUsuario_uP  = request.POST['appaterno']
    apellUsuario_uM  = request.POST['apmaterno']
    correo_u  = request.POST['correo']
    direccion_u  = request.POST['dire']
    fechanaci_u = request.POST['naci']

    User.objects.create_user(id = int(rutUsuario_u), password = conUsuario_u, is_superuser=0,username = rutUsuario_u, first_name = nomUsuario_u, last_name = apellUsuario_uP, email = correo_u, is_staff=0, is_active=1)
    usuario.objects.create(rut_o_pasaporte = rutUsuario_u, nombre = nomUsuario_u, appaterno = apellUsuario_uP, apmaterno = apellUsuario_uM, correo = correo_u, direccion = direccion_u, fecha_nacimiento = fechanaci_u)

    messages.success(request,'La cuenta ha sido creada correctamente')
    return render(request,'RentCar/InicioSesion.html')
    
def registraOrden(request):
    usuarios = User.objects.all()
    datosUser = {"DatosUser" : usuarios}
    
    return render(request,'RentCar/formOrden.html', datosUser)

def registraOrdenV2(request):
    reserva1 = request.POST['reserva']
    inicio1  = request.POST['inicio']
    termino1  = request.POST['termino']
    nro_documento1  = request.POST['nro_documento']
    rutopasaporte1  = request.POST['ruttt']
    patente1  = request.POST['patentee']
    status1  = request.POST['status']
    precio1  = request.POST['valu']

    patente2 = vehiculo.objects.get(patente = patente1)
    status2 =  status.objects.get(id_status = status1)
    rutopasaporte2 = usuario.objects.get(rut_o_pasaporte= rutopasaporte1)

    orden.objects.create(dia_reserva = reserva1, dia_inicio =inicio1, dia_termino = termino1, nro_documento =nro_documento1 , 
    rutPasaporte  = rutopasaporte2, ptente = patente2 , idStatus = status2 ,precio_total_orden =  precio1 )

    return redirect('catalogo_planilla')

#LOGIN
def login_view(request):
    u = request.POST['Rut']
    c = request.POST['clave']

    user = authenticate(username = u, password = c)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request,'Usuario Inactivo')
    else:
        messages.error(request,'Usuario y/o contraseña incorrecta')
        return redirect('acceso')

#LOGOUT
def logout_view(request):
    logout(request)
    return redirect('inicio')

def registarauto(request):

        data = {
            'form': vehiculoForm()
        }
        if request.method == 'POST':
            formulario = vehiculoForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "Agregado correctamente"
            else:
                data["form"] = formulario
        return render(request,"RentCar/pag_form_auto.html", data)

def mod_auto(request, pat):
    vehiculo1 = get_object_or_404(vehiculo, patente=pat)
    
    data1 = {
        'form': vehiculoForm(instance=vehiculo1)
      }
    if request.method == 'POST':
        formulario = vehiculoForm(data=request.POST, instance=vehiculo1,  files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data1["mensaje"] = "Modificado correctamente"
        data1["form"] = formulario
    
    return render(request,"RentCar/mod_auto.html", data1)

def eliminarAuto(request, pat):
    vehiculo1 = get_object_or_404(vehiculo, patente=pat)
    vehiculo1.delete()
    return redirect(to="catalogo_planilla")


def catalogo_planilla(request):
    data = vehiculo.objects.all()
    return render(request, 'RentCar/catalogo_planilla.html',{'vehiculo' : data})

def inicio(request):
    return render(request, 'RentCar/main_page.html')

def informacion(request):
    return render(request, 'RentCar/Pag_info.html')

def perfil(request ):
    return render(request,'RentCar/pagina_perfil.html')
    
def perfil2(request, id ):
    data = usuario.objects.get( rut_o_pasaporte = id)
    return render(request,'RentCar/mod_perfil.html',{'usuario' : data})

def mod_perfil(request, id):
    usuario1 = get_object_or_404(User, username=id )
    data = {
        'form': usuarioForm(instance=usuario1)
      }
    if request.method == 'POST':
        formulario =  usuarioForm(data=request.POST, instance=usuario1)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="inicio")
        data["form"] = formulario

    return render(request, 'RentCar/mod_perfil.html', data)

def ordenes(request):
    ordenes = orden.objects.all()
    dat = {'ordenes': ordenes}
    return render(request, 'RentCar/pag_registro.html', dat)

def eliminarOrden(request, id):
    orden1 = get_object_or_404(orden, id_orden=id)
    orden1.delete()
    return redirect(to="ordenes")

def registro(request):
    return render(request, 'RentCar/pag_formulario.html')

def inicioSesion(request):
    return render(request, 'RentCar/InicioSesion.html')

def info_auto(request, pat):
    data = vehiculo.objects.get( patente = pat)
    return render(request, 'RentCar/info_auto.html', {'vehiculo' : data})