from django import forms
from .models import Denuncia, User, Endereco, DptPublicos


class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = '__all__'


