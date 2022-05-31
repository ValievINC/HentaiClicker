from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import UserForm
from .serializers import UserSerializer
from .models import UserData
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer


class Register(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            core = UserData(user=user)
            core.save()
            return redirect('welcome')
        return render(request, 'register.html', {'form': form})


class Login(APIView):
    form = UserForm()
    def get(self, request):
        return render(request, 'login.html', {'form': self.form})
    def post(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('welcome')
        return render(request, 'login.html', {'form': self.form, 'invalid': True})

@login_required
def index(request):
    user = UserData.objects.get(user=request.user)
    return render(request, 'welcome.html', {'user': user})


def clicker(request):
    return render(request, 'clicker.html', {})


@api_view(['GET'])
@login_required
def call_click(request):
    user = UserData.objects.get(user=request.user)
    user.click()
    user.save()
    return Response({'user': UserSerializer(user).data})

