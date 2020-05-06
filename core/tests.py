from django.test import TestCase
from .models import User, Denuncia
from django.utils import timezone
from .forms import DenunciaForm
from django.urls import reverse


class UserModelTestClass(TestCase):
    @classmethod
    def setUp(self):
        User.objects.create(id=1,nome='Arthur', cpf='05963258799', email="arthur@gmail.com", data_nascimento="2020-08-04")

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

    def test_cpf_max_length(self):
        author = User.objects.get(id=1)
        max_length = author._meta.get_field('cpf').max_length
        self.assertEquals(max_length, 11)


class DenunciaFormTest(TestCase):
    def test_email_field_label(self):
        form = DenunciaForm()
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'e_mail')


class DenunciaViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Denuncia.objects.create(
            titulo = 'Testando a aplicacao',
            texto_denuncia = 'Apenas um teste',
            nome = 'Zezé', 
            email = 'zeze@gmail.com',
            endereco = 'qualquer um',
            bairro = 'Boa vista',
            cidade = 'Recife',
            empresa = 'Comp')
           
    def test_view_url_exists(self):
        response = self.client.get('/cadastrar/denuncia/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('cadastro_denuncia'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('cadastro_denuncia'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro_denuncia.html')