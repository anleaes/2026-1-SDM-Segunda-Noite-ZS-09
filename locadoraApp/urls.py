from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.pessoa.urls')),
    path('api/', include('apps.cliente.urls')),
    path('api/', include('apps.carteira_motorista.urls')),
    path('api/', include('apps.funcionario.urls')),
    path('api/', include('apps.agencia.urls')),
    path('api/', include('apps.categoria_veiculo.urls')),
    path('api/', include('apps.veiculo.urls')),
    path('api/', include('apps.adicional.urls')),
    path('api/', include('apps.seguro.urls')),
    path('api/', include('apps.reserva.urls')),
]



