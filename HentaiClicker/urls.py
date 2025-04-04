from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from Clicker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls', namespace='users')),
    path('clicker/', include('Clicker.urls', namespace='clicker'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
