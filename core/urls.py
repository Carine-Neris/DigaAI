from django.urls import path, include
from .views import home, cadastro_denuncia, SignUp

urlpatterns = [
    path("digaai/", home, name="home"),
    path("cadastrar/denuncia", cadastro_denuncia, name="cadastro_denuncia"),
    path("cadastrar/user", SignUp.as_view(), name="cadastro_user"),
    path("accounts/", include("django.contrib.auth.urls"), name="login"),
]
