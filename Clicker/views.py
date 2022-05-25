from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import UserForm
from .serializers import UserSerializer
from .models import UserData
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        return render(request, 'register.html', {'form': form})
    form = UserForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = UserForm()
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('welcome')
        return render(request, 'login.html', {'form': form, 'invalid': True})
    return render(request, 'login.html', {'form': form})


def index(request):
    return render(request, 'welcome.html', {})


def clicker(request):
    return render(request, 'clicker.html', {})