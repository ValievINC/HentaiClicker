from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .forms import UserForm
from .serializers import UserSerializer
from .models import UserData


# Хз че это, но если убрать, то работать не будет)))
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer


# Непосредственно логика Регистрации
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


# Непосредственно логика Логизации
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


# Непосредственно логика логаутизации
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


# Непосредственно логика клика
@api_view(['GET'])
@login_required
def call_click(request):
    user = UserData.objects.get(user=request.user)
    user.click()
    user.check_level()
    user.save()

    return Response({'user': UserSerializer(user).data})


# Эээ ну как бы показывает на страницу Welcome
@login_required
def index(request):
    user = UserData.objects.get(user=request.user)
    return render(request, 'welcome.html', {'user': user})


# Функция, необходимая для предзагрузки изображения
@api_view(['GET'])
@login_required
def onload_image(request):
    user = UserData.objects.get(user=request.user)
    return Response({'user': UserSerializer(user).data})


# Следующие пять функций описывают логику работы каждой кнопки покупки тентаклины
# Вы можете назвать автора этого дерьма всеми плохими словами, которые найдете в своей голове
# За то, что он не вывел это дело в один единственный класс.
# Но поверьте, у него были на это свои причины. От банального не хочу, до банального не умею
@api_view(['GET'])
@login_required
def update_power1(request):
    user = UserData.objects.get(user=request.user)

    # Проверяем, что хватает денег. Если не хватает, ничего не делаем
    if user.score < user.tentacle1_cost:
        return Response({'user': UserSerializer(user).data})

    # Если денег всё-таки хватило, то
    user.tentacle1_count += 1                               # Количество тентаклей увеличиваем на 1
    user.click_power += 1                                   # Еще и силу клика увеличиваем
    user.score -= user.tentacle1_cost                       # Стоимость тентаклины вычитаем из Счёта
    user.tentacle1_cost = round(user.tentacle1_cost * 1.5)  # Делаем новую стоимость тентаклины
    user.save()                                             # Сохраняем

    return Response({'user': UserSerializer(user).data})    # Внизу всё то же самое


@api_view(['GET'])
@login_required
def update_power2(request):
    user = UserData.objects.get(user=request.user)

    if user.score < user.tentacle2_cost:
        return Response({'user': UserSerializer(user).data})

    user.tentacle2_count += 1
    user.click_power += 5
    user.score -= user.tentacle2_cost
    user.tentacle2_cost = round(user.tentacle2_cost * 1.5)
    user.save()

    return Response({'user': UserSerializer(user).data})


@api_view(['GET'])
@login_required
def update_power3(request):
    user = UserData.objects.get(user=request.user)

    if user.score < user.tentacle3_cost:
        return Response({'user': UserSerializer(user).data})

    user.tentacle3_count += 1
    user.click_power += 25
    user.score -= user.tentacle3_cost
    user.tentacle3_cost = round(user.tentacle3_cost * 1.5)
    user.save()

    return Response({'user': UserSerializer(user).data})


@api_view(['GET'])
@login_required
def update_power4(request):
    user = UserData.objects.get(user=request.user)

    if user.score < user.tentacle4_cost:
        return Response({'user': UserSerializer(user).data})

    user.tentacle4_count += 1
    user.click_power += 125
    user.score -= user.tentacle4_cost
    user.tentacle4_cost = round(user.tentacle4_cost * 1.5)
    user.save()

    return Response({'user': UserSerializer(user).data})


@api_view(['GET'])
@login_required
def update_power5(request):
    user = UserData.objects.get(user=request.user)

    if user.score < user.tentacle5_cost:
        return Response({'user': UserSerializer(user).data})

    user.tentacle5_count += 1
    user.click_power += 625
    user.score -= user.tentacle5_cost
    user.tentacle5_cost = round(user.tentacle5_cost * 1.5)
    user.save()

    return Response({'user': UserSerializer(user).data})


# Эта параша(иначе её не назвать: страшная и воняет) отвечает за вывод циферок на страничку
def clicker(request):
    user = UserData.objects.get(user=request.user)
    userScore = user.score  # Счет юзера
    userHPC = user.click_power  # Сколько юзер делает хитов за клик

    # Кол-во тентаклин
    tentacle1_count = user.tentacle1_count
    tentacle2_count = user.tentacle2_count
    tentacle3_count = user.tentacle3_count
    tentacle4_count = user.tentacle4_count
    tentacle5_count = user.tentacle5_count

    # Стоимость тентаклин
    tentacle1_cost = user.tentacle1_cost
    tentacle2_cost = user.tentacle2_cost
    tentacle3_cost = user.tentacle3_cost
    tentacle4_cost = user.tentacle4_cost
    tentacle5_cost = user.tentacle5_cost

    # Делаем контекст, чтобы выглядело покрасивше(а то в ретюрне будет жопа)
    context = {
        'score': userScore,
        'userHPC': userHPC,
        'tentacle1_count': tentacle1_count,
        'tentacle2_count': tentacle2_count,
        'tentacle3_count': tentacle3_count,
        'tentacle4_count': tentacle4_count,
        'tentacle5_count': tentacle5_count,
        'tentacle1_cost': tentacle1_cost,
        'tentacle2_cost': tentacle2_cost,
        'tentacle3_cost': tentacle3_cost,
        'tentacle4_cost': tentacle4_cost,
        'tentacle5_cost': tentacle5_cost,
    }
    return render(request, 'clicker.html', context)