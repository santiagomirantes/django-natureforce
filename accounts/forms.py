from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    avatar = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(forms.ModelForm):
    avatar = forms.ImageField(label="Nuevo Avatar",required=False)
    email = forms.EmailField(label="Nuevo E-Mail")
    password1 = forms.CharField(label="Nueva contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir nueva contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        help_texts = {k:"" for k in fields}




