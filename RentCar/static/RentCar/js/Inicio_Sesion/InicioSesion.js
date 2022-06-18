$(document).ready(function () {
    $("#form").submit(function (e) {
        e.preventDefault();
        var rut = $("#Rut").val();
        var clave = $("#clave").val();
        var mensaje = "";

        let entrar = false;

        if (rut.trim().length < 4) {
            mensaje += 'El rut o pasaporte no es valido <br>';
            entrar = true;
        }
        if (clave.trim().length < 4 || clave.trim().length > 12) {
            mensaje += 'La clave no es valida <br>';
            entrar = true;
        }
        if (entrar) {
            $("#warnings").html(mensaje);
        } else {
            $("#warnings").html("Aceptado");
        }
    });
})
