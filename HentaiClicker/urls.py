from django.contrib import admin
from django.urls import path
from Clicker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.index, name='welcome'),
    path('hentai_clicker', views.clicker, name='hentai_clicker'),
    path('user_data', views.UserView.as_view(), name='user_data'),
]
