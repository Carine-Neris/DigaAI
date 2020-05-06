from django.shortcuts import render
from .models import Endereco, Denuncia, User, DptPublicos
from .forms import DenunciaForm


def home(request):
    return render(request, 'home.html')


def cadastro_denuncia(request):
    if request.method == "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()

    form = DenunciaForm()
    return render(request, 'cadastro_denuncia.html',{'form':form})