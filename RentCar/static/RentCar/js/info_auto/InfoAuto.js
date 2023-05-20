const parrafo = document.getElementById("error")
              const parrafo1 = document.getElementById("correcto")
              
              $(document).ready(function () {
                  $("#formulario").submit(function (e) {
                      
                      let entrar = false
                      let error = ""
                      let f1 = document.getElementById("inicio").value
                      let f2 = document.getElementById("termino").value
                      let f3 = document.getElementById("precio").value
                      let f4 = document.getElementById("valu").value
                      let f5 = document.getElementById("reserva").value
                      parrafo.innerHTML = ""
                      parrafo1.innerHTML = ""
                      var resultado = "";
                      inicial = inicio.value.split("-");
                      final = termino.value.split("-");
                      var dateStart = new Date(inicial[0], (inicial[1] - 1), inicial[2]);
                      var dateEnd = new Date(final[0], (final[1] - 1), final[2]);
                      var diasDif = dateEnd.getTime() - dateStart.getTime();
                      valor1 = (diasDif/ 86400000)*precio.value;
              
              
                      if (inicio.value > termino.value) {
                          error += 'La fecha de inicio no puede ser mayor a la de término'
                          entrar = true
                      }
                      if (inicio.value == termino.value) {
                          error += 'El arriendo debe ser mínimo de un día'
                          entrar = true
                      }
                      if (precio.value > valu.value){
                          error += 'El precio no coincide con el calculado'
                          entrar = true
                      }
              
                      if (precio.value <  valu.value){
                          error =+ 'El precio no coincide con el calculado'
                          entrar = true
                      }
              
                      if (entrar) {
                          parrafo.innerHTML = error
                      }
                      else {
                          parrafo1.innerHTML = "¡El auto ha sido arrendado!"
              
                      }
                      e.preventDefault();
                  })
              
              });
              
              inicio.min = new Date().toISOString().split("T")[0];
              termino.min = new Date().toISOString().split("T")[0];
              reserva.min = new Date().toISOString().split("T")[0];
              reserva.max = new Date().toISOString().split("T")[0];