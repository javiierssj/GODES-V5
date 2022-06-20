from django import forms
from  .models import vehiculo, usuario
class vehiculoForm(forms.ModelForm):

    #idModelo = forms.ChoiceField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'modelo'}))
    patente = forms.CharField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'patente'}))
    nro_chasis = forms.CharField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Nro chasis'}))
    color = forms.CharField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Color'}))
    estado = forms.CharField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Estado'}))
    asientos = forms.CharField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Estado'}))
    kilos = forms.CharField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Estado'}))
    nro_motor = forms.CharField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Estado'}))
    precio_vehiculo = forms.DecimalField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Estado'}))
    rendimiento = forms.CharField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Estado'}))
    motor = forms.CharField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Estado'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"class":"controls",'placeholder':'Estado'}))
    class Meta:
        model = vehiculo
        fields = '__all__'

class usuarioForm(forms.ModelForm):

    class Meta:
        model = usuario
        fields = ["nombre", "appaterno",  "apmaterno", "direccion"]