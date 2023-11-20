from django.urls import path, include
from .views import *

app_name = "authapp"

urlpatterns = [
    path("login" , home , name="login")
]