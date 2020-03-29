from django.urls import path
from .views import home, cadastro_denuncia

urlpatterns = [
    path('digaai/', home, name='home'),
    path('cadastrar/denuncia', cadastro_denuncia, name='cadastro_denuncia'),
]
