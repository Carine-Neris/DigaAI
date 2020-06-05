from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
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


class SignUp(generic.CreateView):
    form_class = FormUsuario
    sucess_url = reverse_lazy("login")
    template_name = "register.html"
