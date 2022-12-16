from django.urls import path
from Clicker.views import ClickerPlayView
from django.contrib.auth.decorators import login_required

app_name = 'Clicker'

urlpatterns = [
    path('play/', login_required(ClickerPlayView.as_view()), name='play'),
]