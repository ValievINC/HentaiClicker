from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import UserForm
from .serializers import UserSerializer
from .models import UserData


class UserView(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        if id:
            user = UserData.objects.filter(pk=id)
            return Response(user.values())
        users = UserData.objects.all()
        return Response(users.values())

    def post(self, request):
        score = request.data.get('score')
        click_power = request.data.get('click_power')
        if score and click_power:
            users = UserData.objects.create(score=score, click_power=click_power)
            return Response({
                'id': UserData.id,
                'score': UserData.score,
                'click_power': UserData.click_power,
            })
        return Response({"Error": "Invalid data"})

    def put(self, request):
        id = request.data.get('id')
        if id:
            user = UserData.objects.filter(pk = id)
            user.update(
                score = request.data.get('score'),
                click_power = request.data.get('click_power')
            )
            return Response({
                'id': UserData.id,
                'score': UserData.score,
                'click_power': UserData.click_power,
            })
        return Response({"Error": "Invalid data"})

    def delete(self, request):
        id = request.query_params.get('id')
        if id:
            user = UserData.objects.get(pk=id)
            user.delete()
            return Response({'Response': f'user {user.id} deleted'})
        return Response({"Error": "Invalid data"})



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