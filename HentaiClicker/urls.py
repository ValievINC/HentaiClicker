from django.contrib import admin
from django.urls import path
from Clicker import views
from Clicker.views import Register, Login

users_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
users_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('', views.index, name='welcome'),
    path('hentai_clicker', views.clicker, name='hentai_clicker'),
    path('api/users_viewset/', users_list, name='users_viewset'),
    path('api/users_viewset/<int:pk>/', users_detail, name='users_viewset'),
    path('call_click/', views.call_click),
    path('onload_image/', views.onload_image),
    path('update_power1', views.update_power1),
    path('update_power2', views.update_power2),
    path('update_power3', views.update_power3),
    path('update_power4', views.update_power4),
    path('update_power5', views.update_power5),
]
