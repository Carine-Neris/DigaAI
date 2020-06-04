from django.urls import path, include
from .views import home, cadastro_denuncia, cadastro_user

urlpatterns = [
    path("digaai/", home, name="home"),
    path("cadastrar/denuncia", cadastro_denuncia, name="cadastro_denuncia"),
    path("cadastrar/user", cadastro_user, name="cadastro_user"),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls"), name="login"),
]
