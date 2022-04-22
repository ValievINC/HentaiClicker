from django.contrib import admin
from django.urls import path
from Clicker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='welcome'),
    path('hentai_clicker', views.clicker, name='hentai_clicker')
]
