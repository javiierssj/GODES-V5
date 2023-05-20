from django import forms
from  .models import vehiculo
from django.contrib.auth.models import User
class vehiculoForm(forms.ModelForm):

    #idModelo = forms.ChoiceField(widget=forms.TextInput(attrs={"class":"controls",'placeholder':'modelo'}))
    #tidModelo = forms.ModelChoiceField(queryset=vehiculo.objects.all())

    patente = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Patente'})
    )
    nro_chasis = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Nro de chasis'})
    )
    color = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Color'})
    )
    estado = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Estado'})
    )
    asientos = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Asientos'})
    )
    kilos = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Kilos'})
    )
    nro_motor = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Numero del motor'})
    )
    precio_vehiculo = forms.DecimalField( 
    label="",
    widget=forms.NumberInput(attrs={"class":"controls",'placeholder':'Precio'})
    )
    rendimiento = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Rendimiento'})
    )
    motor = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Motor'})
    )
    descripcion = forms.CharField( 
    label="",
    widget=forms.Textarea(attrs={"class":"controls",'placeholder':'Descripción'})
    )
    imagen1 = forms.ImageField(
        label="Imagen 1",
    )
    imagen2 = forms.ImageField(
        label="Imagen 2",
    )
    imagen3 = forms.ImageField(
        label="Imagen 3",
    )

    class Meta:
        model = vehiculo
        fields = '__all__'

class usuarioForm(forms.ModelForm):

    first_name = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Patente'})
    )
    last_name = forms.CharField( 
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':'Patente'})
    )
    email = forms.EmailField(
    label="",
    widget=forms.TextInput(attrs={"class":"controls",'placeholder':""})
    )

    class Meta:
        model = User
        fields = ["first_name","last_name","email"]