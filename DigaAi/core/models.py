from django.db import models


class User(models.Model):
    nome = models.CharField(max_length=50, null=False,blank=False)
    cpf = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    data_nascimento = models.DateTimeField()
    cep = models.IntegerField()


    def __str__(self):
        return self.nome


class DptPublicos(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    tel = models.CharField(max_length=9, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)


    def __str__(self):
        return self.nome


class Endereco(models.Model):
    rua = models.CharField(max_length=50, null=False, blank=False)
    numero = models.SmallIntegerField(null=False, blank=False)
    cep = models.SmallIntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)


    def __str__(self):
        return self.rua

class Denuncia(models.Model):
    titulo = models.CharField(max_length= 100, null=False, blank=False)
    texto_denuncia = models.TextField(max_length=1500, null=False, blank=False)
    denunciante = models.ForeignKey(User,on_delete=models.CASCADE, null=False, blank=False)
    dpt_publico = models.ForeignKey(DptPublicos,on_delete=models.CASCADE,null=False, blank=False)
    endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE,null=False, blank=False)

    def __str__(self):
        return self.titulo


