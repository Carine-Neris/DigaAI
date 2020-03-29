from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def cadastro_denuncia(request):
    return render(request, 'cadastro_denuncia.html')
