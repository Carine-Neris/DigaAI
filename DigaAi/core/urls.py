from django.urls import path
from .views import *


urlpatterns = [
    path('', hello, name='user'),
]