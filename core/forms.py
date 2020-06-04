from django import forms
from django.contrib.auth.models import User
from .models import Denuncia, DptPublico


class DenunciaForm(forms.ModelForm):
    titulo = forms.CharField(required=True, max_length=100,)
    nome = forms.CharField(required=False, max_length=50)
    email = forms.EmailField(help_text="Opcional")

    class Meta:
        model = Denuncia
        fields = "__all__"


class FormUsuario(forms.Form):

    username = forms.CharField(max_length=200, label="username")
    email = forms.CharField(max_length=50, label="e_mail")
    first_name = forms.CharField(max_length=200, label="nome")
    last_name = forms.CharField(max_length=50, label="sobrenome")
    password = forms.CharField(max_length=50, label="senha")

    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password")
        models = User
