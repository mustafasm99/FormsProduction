from django.urls import path, include
from .views import *
app_name = 'DASHBORD'

urlpatterns = [
    path('' , home , name='home'),
    path('data/<str:formName>' , show_form_data , name="formname"),
    path('<str:uuid>',get_old_forms , name="get_old_forms"),
    path('edit/<str:formname>' , edit_form , name="editform"),
    path('show/<str:formname>', show_form , name="showform")
]