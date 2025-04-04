from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from users.forms import LoginForm, RegistrationForm
from users.models import User


class UserRegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class UserWelcomeView(TemplateView):
    template_name = 'welcome.html'
