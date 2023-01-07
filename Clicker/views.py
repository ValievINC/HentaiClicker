from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from Clicker.models import Tentacles, Results


def clicker_view(request):
    context = {
        'results': Results.objects.filter(user=request.user),
        'tentacles': Tentacles.objects.all()
    }
    return render(request, 'clicker.html', context)


def onload_image(request):
    result = Results.objects.get(user=request.user)
    return HttpResponseRedirect(result)


def call_click(request):
    result = Results.objects.get(user=request.user)
    result.click()
    result.check_level()
    result.save()
    return HttpResponseRedirect(request.path_info)

# class ClickerPlayView(ListView):
#     model = Results
#     template_name = 'clicker.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ClickerPlayView, self).get_context_data()
#         context['results_list'] = Results.objects.filter(user=self.request.user)
#         return context

# @api_view(['GET'])
# @login_required
# def onload_image(request):
#     user = UserData.objects.get(user=request.user)
#     return Response({'user': UserSerializer(user).data})
#
#
# @api_view(['GET'])
# def call_click(request):
#     user = UserData.objects.get(user=request.user)
#     user.click()
#     user.check_level()
#     user.save()
#
#     return Response({'user': UserSerializer(user).data})
# @api_view(['GET'])
# @login_required
# def update_power1(request):
#     user = UserData.objects.get(user=request.user)
#
#     # Проверяем, что хватает денег. Если не хватает, ничего не делаем
#     if user.score < user.tentacle1_cost:
#         return Response({'user': UserSerializer(user).data})
#
#     # Если денег всё-таки хватило, то
#     user.tentacle1_count += 1                               # Количество тентаклей увеличиваем на 1
#     user.click_power += 1                                   # Еще и силу клика увеличиваем
#     user.score -= user.tentacle1_cost                       # Стоимость тентаклины вычитаем из Счёта
#     user.tentacle1_cost = round(user.tentacle1_cost * 1.5)  # Делаем новую стоимость тентаклины
#     user.save()                                             # Сохраняем
#
#     return Response({'user': UserSerializer(user).data})    # Внизу всё то же самое
#
#
# @api_view(['GET'])
# @login_required
# def update_power2(request):
#     user = UserData.objects.get(user=request.user)
#
#     if user.score < user.tentacle2_cost:
#         return Response({'user': UserSerializer(user).data})
#
#     user.tentacle2_count += 1
#     user.click_power += 5
#     user.score -= user.tentacle2_cost
#     user.tentacle2_cost = round(user.tentacle2_cost * 1.5)
#     user.save()
#
#     return Response({'user': UserSerializer(user).data})
#
#
# @api_view(['GET'])
# @login_required
# def update_power3(request):
#     user = UserData.objects.get(user=request.user)
#
#     if user.score < user.tentacle3_cost:
#         return Response({'user': UserSerializer(user).data})
#
#     user.tentacle3_count += 1
#     user.click_power += 25
#     user.score -= user.tentacle3_cost
#     user.tentacle3_cost = round(user.tentacle3_cost * 1.5)
#     user.save()
#
#     return Response({'user': UserSerializer(user).data})
#
#
# @api_view(['GET'])
# @login_required
# def update_power4(request):
#     user = UserData.objects.get(user=request.user)
#
#     if user.score < user.tentacle4_cost:
#         return Response({'user': UserSerializer(user).data})
#
#     user.tentacle4_count += 1
#     user.click_power += 125
#     user.score -= user.tentacle4_cost
#     user.tentacle4_cost = round(user.tentacle4_cost * 1.5)
#     user.save()
#
#     return Response({'user': UserSerializer(user).data})
#
#
# @api_view(['GET'])
# @login_required
# def update_power5(request):
#     user = UserData.objects.get(user=request.user)
#
#     if user.score < user.tentacle5_cost:
#         return Response({'user': UserSerializer(user).data})
#
#     user.tentacle5_count += 1
#     user.click_power += 625
#     user.score -= user.tentacle5_cost
#     user.tentacle5_cost = round(user.tentacle5_cost * 1.5)
#     user.save()
#
#     return Response({'user': UserSerializer(user).data})
#
#
# # Эта параша(иначе её не назвать: страшная и воняет) отвечает за вывод циферок на страничку
