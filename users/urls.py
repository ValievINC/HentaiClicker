from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import UserRegisterView, UserLoginView, UserWelcomeView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('welcome/', login_required(UserWelcomeView.as_view()), name='welcome'),
]