from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

#los datos de los forms se deben poner en español para que el usuario los vea así

class AddPhotoForm(forms.Form):
    nombre = forms.CharField(max_length = 100)
    año = forms.IntegerField()
    archivo = forms.FileField()
    artista = forms.CharField(max_length = 100)

class AddArtistForm(forms.Form):
    nombre = forms.CharField(max_length = 100)
    edad = forms.IntegerField()
    email = forms.EmailField()

class AddUserForm(forms.Form):
    foto = forms.FileField(required=False, label="Foto (opcional)")
    nombre = forms.CharField(max_length = 100)
    email = forms.EmailField()    