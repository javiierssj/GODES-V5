$(document).ready(function () {
    $("#form").submit(function (e) {
        e.preventDefault();
        var nombre = $("#nombre").val();
        var clave = $("#clave").val();
        var appaterno = $("#apellido_p").val();
        var apmaterno = $("#apellido_m").val();
        var direc = $("#direccion").val();
        var clave1 = $("#clave1").val();

        var mensaje = "";

        let entrar = false;



        if (nombre.trim().length < 4 || nombre.trim().length > 12) {
            mensaje += 'El nombre no es valido, debe ser entre 4 y 12 caracteres.<br>';
            entrar = true;
        }
        if (appaterno.trim().length < 3 || appaterno.trim().length > 15) {
            mensaje += 'El apellido paterno no es valido, debe ser entre 4 y 12 caracteres.<br>';
            entrar = true;
        }
        if (apmaterno.trim().length < 3 || apmaterno.trim().length > 15) {
            mensaje += 'El apellido materno no es valido, debe ser entre 4 y 12 caracteres.<br>';
            entrar = true;
        }
        if (direc.trim().length < 4 || direc.trim().length > 30) {
            mensaje += 'La direccion no es valida, debe ser entre 4 y 30 caracteres.<br>';
            entrar = true;
        }
        if (clave.trim().length < 4 || clave.trim().length > 12) {
            mensaje += 'La clave no es valida, debe ser entre 4 y 12 caracteres.<br>';
            entrar = true;
        }
        if (clave1.trim().length < 4 || clave1.trim().length > 12) {
            mensaje += 'La clave no es valida, debe ser entre 4 y 12 caracteres.<br>';
            entrar = true;
        }





        /Validacion Mayusculas/

        var letraValidar = nombre.charAt(0);
        if (!esMayuscula(letraValidar)) {
            mensaje += 'La primera letra de el nombre debe ser mayuscula. <br>';
            entrar = true;
        }
        var letraValidar = appaterno.charAt(0);
        if (!esMayuscula(letraValidar)) {
            mensaje += 'La primera letra de el apellido paterno debe ser mayuscula. <br>';
            entrar = true;
        }
        var letraValidar = apmaterno.charAt(0);
        if (!esMayuscula(letraValidar)) {
            mensaje += 'La primera letra de el apellido materno debe ser mayuscula. <br>';
            entrar = true;
        }
        /Validacion numeros /
        var corte1 = $("#clave").val();
        var contar_numeros = corte1.replace(/[^0-9]/g, "").length;

        if (contar_numeros == 0) {
            mensaje += 'Falta al menos un numero en la contraseña.<br>';
            entrar = true;
        }
        if (contar_numeros == clave.trim().length) {
            mensaje += 'La contraseña no debe ser solo numeros.<br>'
            entrar = true;


        }



        /Validacion mayuscula/
        var letraValidar = clave.charAt(0);
        if (!esMayuscula(letraValidar)) {
            mensaje += 'La primera letra de la clave debe ser mayuscula. <br>';
            entrar = true;
        }

        /Validacion espacios/


        var espacios = false;
        var cont = 0;

        while (!espacios && (cont < clave.length)) {
            if (clave.charAt(cont) == " ")
                espacios = true;
            cont++;
        }

        if (espacios) {
            mensaje += 'La contraseña no debe contener espacios. <br>' ;
            
            espacios=false;
            entrar=true;
        }
        /*Clave 2 */
        /Validacion numeros /
        var corte1 = $("#clave1").val();
        var contar_numeros = corte1.replace(/[^0-9]/g, "").length;

        if (contar_numeros == 0) {
            mensaje += 'Falta al menos un numero en la contraseña.<br>';
            entrar = true;
        }
        if (contar_numeros == clave1.trim().length) {
            mensaje += 'La contraseña no debe ser solo numeros.<br>'
            entrar = true;


        }



        /Validacion mayuscula/
        var letraValidar = clave1.charAt(0);
        if (!esMayuscula(letraValidar)) {
            mensaje += 'La primera letra de la clave debe ser mayuscula. <br>';
            entrar = true;
        }

        /Validacion espacios/


        var espacios = false;
        var cont = 0;

        while (!espacios && (cont < clave1.length)) {
            if (clave1.charAt(cont) == " ")
                espacios = true;
            cont++;
        }

        if (espacios) {
            mensaje += 'La contraseña no debe contener espacios. <br>' ;
            
            espacios=false;
            entrar=true;
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


