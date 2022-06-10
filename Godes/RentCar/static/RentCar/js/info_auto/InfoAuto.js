
const parrafo = document.getElementById("error")
const parrafo1 = document.getElementById("correcto")

$(document).ready(function () {
    $("#formulario").submit(function (e) {
        e.preventDefault();
        let entrar = false
        let error = ""
        let f1 = document.getElementById("inicio").value
        let f2 = document.getElementById("termino").value
        parrafo.innerHTML = ""
        parrafo1.innerHTML= ""
        if (inicio.value > termino.value){
            error += 'La fecha de inicio no puede ser mayor a la de término'
            entrar = true
        }
        if(inicio.value == termino.value){
            error += 'El arriendo debe ser mínimo de un día'
            entrar = true
        }
        if(entrar){
            parrafo.innerHTML = error
        }
        else{
             parrafo1.innerHTML = "¡El auto ha sido arrendado!"
          
        }
    })
});




inicio.min = new Date().toISOString().split("T")[0];
termino.min = new Date().toISOString().split("T")[0];

