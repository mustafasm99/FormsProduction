from django.urls import path, include
from .views import allTeacher

app_name = "student"
urlpatterns = [
   path('courses' , allTeacher , name='home')
]