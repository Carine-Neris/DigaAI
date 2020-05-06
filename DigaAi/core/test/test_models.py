from django.test import TestCase
from ..models import User


class UserModelTestClass(TestCase):
    @classmethod
    def setUp(self):
        User.objects.create(nome='Arthur', cpf='05963258799', email="arthur@gmail.com", data_nascimento="2020-08-04", cep=50090590)


    def test_first_name_label(self):
        usuario = User.objects.get(id=1)
        field_label = usuario._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')

    def test_email_label(self):
        usuario = User.objects.get(id=1)
        field_label = usuario._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_first_name_max_length(self):
        author = User.objects.get(id=1)
        max_length = author._meta.get_field('nome').max_length
        self.assertEquals(max_length, 50)