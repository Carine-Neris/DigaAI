from django.shortcuts import render
from .models import Denuncia, DptPublico
from django.contrib.auth.models import User
from .forms import DenunciaForm, FormUsuario


def home(request):
    return render(request, "home.html")


def cadastro_denuncia(request):
    if request.method == "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()

    form = DenunciaForm()
    return render(request, "cadastro_denuncia.html", {"form": form})


def cadastro_user(request):
    if request.method == "POST":
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
    form = FormUsuario()
    return render(request, "cadastro_user.html", {"form": form})
