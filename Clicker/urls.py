from django.urls import path
from Clicker import views
from django.contrib.auth.decorators import login_required

app_name = 'clicker'

urlpatterns = [
    path('play/', login_required(views.clicker_view), name='play'),
    path('call_click/', views.call_click, name='call_click'),
    path('onload_image/', views.onload_image, name='onload'),
]