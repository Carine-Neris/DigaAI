from django import forms
from .models import Denuncia, User, Endereco, DptPublicos


class DenunciaForm(forms.ModelForm):
    titulo = forms.CharField(required=True,max_length=100,)
    nome = forms.CharField(required=False, max_length=50, label="e-mail")
    email = forms.EmailField()

    class Meta:
        model = Denuncia
        fields = '__all__'


