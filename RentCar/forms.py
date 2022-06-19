from django import forms
from  .models import vehiculo, usuario
class vehiculoForm(forms.ModelForm):

    class Meta:
        model = vehiculo
        fields = '__all__'

class usuarioForm(forms.ModelForm):

    class Meta:
        model = usuario
        fields = ["nombre", "appaterno",  "apmaterno", "direccion"]