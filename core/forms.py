from django import forms
from .models import Denuncia, DptPublico


class DenunciaForm(forms.ModelForm):
    titulo = forms.CharField(required=True, max_length=100,)
    email = forms.EmailField(help_text="Opcional")

    class Meta:
        model = Denuncia
        fields = "__all__"
