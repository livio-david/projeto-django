
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro.urls')),
    path('cadastrar/', include('cadastro.urls')),
    path('cadastradas/', include('cadastro.urls')),
]
