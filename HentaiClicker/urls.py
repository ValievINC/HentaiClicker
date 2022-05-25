from django.contrib import admin
from django.urls import path
from Clicker import views

users_list = views.UserViewSet.as_view({
    'get': 'list', # получить список всех заметок
    'post': 'create', # создать заметку
})
users_detail = views.UserViewSet.as_view({
    'get': 'retrieve', # получить данные об одной заметке
    'put': 'update', # обновить все поля заметки
    'patch': 'partial_update', # обновить несколько полей заметки
    'delete': 'destroy' # ремувнуть, уничтожить, удалить, разрушить, зарезать заметку
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.index, name='welcome'),
    path('hentai_clicker', views.clicker, name='hentai_clicker'),
    path('api/users_viewset/', users_list, name='users_viewset'),
    path('api/users_viewset/<int:pk>/', users_detail, name='users_viewset'),
]
