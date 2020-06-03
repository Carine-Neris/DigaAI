from django.db import models
from django.contrib.auth.models import User
from datetime import date


class DptPublico(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    tel = models.CharField(max_length=9, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome


class Denuncia(models.Model):
    dpt_publico = models.ForeignKey(
        DptPublico, on_delete=models.CASCADE, null=False, blank=False
    )
    titulo = models.CharField(max_length=100, null=False, blank=False)
    texto_denuncia = models.TextField(max_length=1500, null=False, blank=False)
    endereco = models.CharField(max_length=50, null=False, blank=True)
    bairro = models.CharField(max_length=50, null=False, blank=True)
    cidade = models.CharField(max_length=50, null=False, blank=True)
    nome = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)

    DENUNCIA_STATUS = (
        ("AB", "Aberta"),
        ("EM", "Em Andamento"),
        ("FE", "Fechada"),
        ("EA", "Em Acompanhamento"),
    )

    status = models.CharField(
        max_length=2,
        choices=DENUNCIA_STATUS,
        blank=True,
        default="AB",
        help_text="Status Da Denuncia",
    )

    def __str__(self):
        return self.titulo
