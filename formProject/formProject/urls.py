from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from form.views import home_page

urlpatterns = [
    path('form/',include('form.url')),
    path('student/',include('student.url')),
    path('admin/', admin.site.urls),
    path('dashbord/' , include('DASHBORD.urls')),
    path("",home_page,name="home"),
    path("" , include("authapp.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)