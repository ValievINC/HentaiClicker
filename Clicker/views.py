from django.shortcuts import render


def index(request):
    return render(request, 'welcome.html', {})


def clicker(request):
    return render(request, 'clicker.html', {})