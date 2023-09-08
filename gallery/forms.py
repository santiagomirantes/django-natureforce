from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

#los datos de los forms se deben poner en español para que el usuario los vea así

class AddPhotoForm(forms.Form):
    nombre = forms.CharField(max_length = 100)
    año = forms.IntegerField()
    archivo = forms.FileField()
    artista = forms.CharField(max_length = 100)
    descripcion = forms.CharField(max_length = 1000, widget=forms.TextInput())

class AddArtistForm(forms.Form):
    nombre = forms.CharField(max_length = 100)
    edad = forms.IntegerField()
    email = forms.EmailField()

class EditPhotoForm(forms.Form):
    nombre = forms.CharField(max_length = 100)
    año = forms.IntegerField()
    archivo = forms.FileField(required=False)
    artista = forms.CharField(max_length = 100)
    descripcion = forms.CharField(max_length = 1000, widget=forms.TextInput())
