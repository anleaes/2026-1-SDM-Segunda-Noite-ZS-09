from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.pessoa.urls')),
    path('api/', include('apps.cliente.urls')),
    path('api/', include('apps.carteira_motorista.urls')),
]
