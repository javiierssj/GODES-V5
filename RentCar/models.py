from django.db import models

# Create your models here.

class rol(models.Model):
    id_rol = models.IntegerField(primary_key=True, verbose_name="Id del rol")
    nombre_rol = models.CharField(max_length=10, verbose_name="Nombre del rol", blank=False, null=False)
    def __str__(self):
        return self.nombre_rol

class marca(models.Model):
    id_marca = models.IntegerField(primary_key=True, verbose_name="Id de la marca")
    nombre_marca = models.CharField(max_length=50, verbose_name="Nombre de la marca", blank=False, null=False)
    def __str__(self):
        return self.nombre_marca

class modelo(models.Model):
    id_modelo = models.IntegerField(primary_key=True, verbose_name="Id del modelo")
    nombre_modelo = models.CharField(max_length=50, verbose_name="Nombre del modelo", blank=False, null=False)
    IdMarca = models.ForeignKey(marca, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_modelo  

class region(models.Model):
    id_region = models.IntegerField(primary_key=True, verbose_name="Id de la region")
    nombre_region = models.CharField(max_length=30, verbose_name="Nombre de la region", blank=False, null=False)
    def __str__(self):
        return self.nombre_region  
     

class comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True, verbose_name="Id de la comuna")
    nombre_comuna = models.CharField(max_length=30, verbose_name="Nombre de la comuna", blank=False, null=False)
    idRegion = models.ForeignKey(region, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_comuna  

class status(models.Model):
    id_status = models.IntegerField(primary_key=True, verbose_name="Id del status")
    nombre_status = models.CharField(max_length=25, verbose_name="Nombre del status", blank=False, null=False)
    def __str__(self):
        return self.nombre_status  


class usuario(models.Model):
    rut_o_pasaporte = models.CharField(verbose_name="Identifiacion de la perrsona", primary_key=True, max_length=20)
    contra_cliente = models.CharField(max_length=10)
    nombre = models.CharField(verbose_name="nombre de la persona",max_length=25)
    appaterno = models.CharField(verbose_name="apellido paterno de la persona",max_length=25)
    apmaterno = models.CharField(verbose_name="apellido materno de la persona",max_length=25)
    fecha_nacimiento = models.DateField(verbose_name="fecha de nacimiento del cliente")
    correo = models.CharField(verbose_name="correo de la persona",max_length=100)
    direccion = models.CharField(verbose_name="direccion de la persona",max_length=100) 
    def __str__(self):
        return self.nombre 

class vehiculo(models.Model):
    idModelo = models.ForeignKey(modelo, on_delete=models.CASCADE)
    patente = models.CharField(primary_key=True, verbose_name="Patente vehiculo", max_length=6)
    nro_chasis = models.CharField(max_length=17, verbose_name="Nro chasis", blank=False, null=False)
    color = models.CharField(max_length=25, verbose_name="Color vehiculo", blank=False, null=False)
    estado = models.CharField(max_length=17, verbose_name="Estado del vehiculo, disponible o no disponible", blank=False, null=False)
    asientos = models.CharField(max_length=10, verbose_name="Numero de asientos del vehiculo", blank=False, null=False)
    kilos = models.CharField(max_length=10, verbose_name="Kilos del vehiculo", blank=False, null=False)
    nro_motor = models.CharField(max_length=10, verbose_name="Numero del motor del vehiculo", blank=False, null=False)
    precio_vehiculo = models.IntegerField(verbose_name="Precio del vehiculo")
    rendimiento = models.CharField(max_length=25, verbose_name="rendimiento del vehiculo en kms", blank=False, null=False)
    motor = models.CharField(max_length=10, verbose_name="lts motor y caballos de fuerza", blank=False, null=False)
    descripcion = models.TextField(verbose_name="descripcion del vehiculo", blank=False, null=False)
    imagen1 = models.ImageField(upload_to="vehiculos", null=False)
    imagen2 = models.ImageField(upload_to="vehiculos", null=False)
    imagen3 = models.ImageField(upload_to="vehiculos", null=False)

    def __str__(self):
        return self.patente  
    

class orden(models.Model):
    id_orden = models.AutoField(primary_key=True, verbose_name="Autoincrementable de la orden")
    dia_reserva = models.DateField(verbose_name="El dia en el que se hizo la reserva")
    dia_inicio = models.DateField(verbose_name="Dia de inicio de el arriendo")
    dia_termino = models.DateField(verbose_name="Dia de termino de el arriendo")
    nro_documento = models.IntegerField (verbose_name="Nro de identificacion")
    rutPasaporte = models.ForeignKey(usuario, on_delete = models.CASCADE)
    ptente= models.ForeignKey(vehiculo, on_delete=models.CASCADE)
    idStatus = models.ForeignKey(status, on_delete=models.CASCADE)
    precio_total_orden = models.IntegerField(verbose_name="Precio total de la orden")
    def __str__(self):
        return self.id_orden 
