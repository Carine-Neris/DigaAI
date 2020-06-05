from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Denuncia, DptPublico


class DenunciaForm(forms.ModelForm):
    titulo = forms.CharField(required=True, max_length=100,)
    nome = forms.CharField(required=False, max_length=50)
    email = forms.EmailField(help_text="Opcional")

    class Meta:
        model = Denuncia
        fields = "__all__"


class FormUsuario(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
        )
        model = User
