
from django.contrib import admin
from django.urls import include,path
from miweb.views import index, about, welcome, contact, success


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('welcome/', welcome, name='welcome'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('accounts/', include('django.contrib.auth.urls')),
]