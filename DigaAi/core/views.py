from django.shortcuts import render
from .models import Endereco, Denuncia, User, DptPublicos
from .forms import DenunciaForm


def home(request):
    return render(request, 'home.html')


def cadastro_denuncia(request):
    form = DenunciaForm()

    return render(request, 'cadastro_denuncia.html',{'form':form})