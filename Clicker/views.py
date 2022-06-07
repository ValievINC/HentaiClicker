from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .forms import UserForm
from .serializers import UserSerializer
from .models import UserData


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


@api_view(['GET'])
@login_required
def onload_image(request):
    user = UserData.objects.get(user=request.user)
    return Response({'user': UserSerializer(user).data})


@api_view(['GET'])
@login_required
def call_click(request):
    user = UserData.objects.get(user=request.user)
    user.click()
    user.save()
    return Response({'user': UserSerializer(user).data})


@api_view(['GET'])
@login_required
def update_power1(request):
    user = UserData.objects.get(user=request.user)
    user.tentacle1_count += 1
    user.click_power += 1
    user.save()
    return Response({'user': UserSerializer(user).data})

@api_view(['GET'])
@login_required
def update_power2(request):
    user = UserData.objects.get(user=request.user)
    user.tentacle2_count += 1
    user.click_power += 5
    user.save()
    return Response({'user': UserSerializer(user).data})

@api_view(['GET'])
@login_required
def update_power3(request):
    user = UserData.objects.get(user=request.user)
    user.tentacle3_count += 1
    user.click_power += 25
    user.save()
    return Response({'user': UserSerializer(user).data})

@api_view(['GET'])
@login_required
def update_power4(request):
    user = UserData.objects.get(user=request.user)
    user.tentacle4_count += 1
    user.click_power += 125
    user.save()
    return Response({'user': UserSerializer(user).data})

@api_view(['GET'])
@login_required
def update_power5(request):
    user = UserData.objects.get(user=request.user)
    user.tentacle5_count += 1
    user.click_power += 625
    user.save()
    return Response({'user': UserSerializer(user).data})

def clicker(request):
    user = UserData.objects.get(user=request.user)
    userScore = user.score
    userHPC = user.click_power
    tentacle1 = user.tentacle1_count
    tentacle2 = user.tentacle2_count
    tentacle3 = user.tentacle3_count
    tentacle4 = user.tentacle4_count
    tentacle5 = user.tentacle5_count
    context = {
        'score': userScore,
        'userHPC': userHPC,
        'tentacle1_count': tentacle1,
        'tentacle2_count': tentacle2,
        'tentacle3_count': tentacle3,
        'tentacle4_count': tentacle4,
        'tentacle5_count': tentacle5
    }
    return render(request, 'clicker.html', context)