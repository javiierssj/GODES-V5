$(document).ready(function () {
    $("#form").submit(function (e) {
        e.preventDefault();
        var patente = $("#Patente").val();
        var nro_chasis = $("#Nro_Chasis").val();
        var color = $("#Color").val();
        var asientos = $("#Asientos").val();
        var kilos = $("#Kilos").val();
        var nro_motor = $("#Nro_Motor").val();
        var precio = $("#Precio").val();

        var mensaje = "";

        let entrar = false;



        if (patente.trim().length != 6) {
            mensaje += 'La patente solo tiene que ser de 6 caracteres.<br>';
            entrar = true;
        }

        if (nro_chasis.trim().length != 17) {
            mensaje += 'El numero de chasis debe ser de 17 caracteres.<br>';
            entrar = true;
        }

        if (color.trim().length < 2) {
            mensaje += 'El color debe tener al menos 2 caracteres.<br>';
            entrar = true;
        }

        if (asientos.trim().length > 10) {
            mensaje += 'El campo asientos debe ser menor a 10 caracteres.<br>';
            entrar = true;
        }

        if (kilos.trim().length > 10) {
            mensaje += 'El campo kilos debe ser menor a 10 caracteres.<br>';
            entrar = true;
        }

        if (nro_motor.trim().length != 10) {
            mensaje += 'El numero de motor debe ser de 10 caracteres.<br>';
            entrar = true;
        }

        /validacion precio/
        var corte1 = $("#Precio").val();
        var contar_numeros = corte1.replace(/[^0-9]/g, "").length;

        if (contar_numeros != precio.trim().length) {
            mensaje += 'El precio deben ser solo numeros.<br>'
            entrar = true;


        }
        



        
        if (entrar) {
            $("#warnings").html(mensaje);
        } else {
            $("#warnings").html("Enviado");
        }

        

    });

    function esMayuscula(letra) {
        return letra === letra.toUpperCase();
    } 
})