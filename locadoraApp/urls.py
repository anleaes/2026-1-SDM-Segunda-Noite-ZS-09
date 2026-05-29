from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.adicional.views import AdicionalViewSet
from apps.agencia.views import AgenciaViewSet
from apps.carteira_motorista.views import CarteiraMotoristaViewSet
from apps.categoria_veiculo.views import CategoriaVeiculoViewSet
from apps.cliente.views import ClienteViewSet
from apps.funcionario.views import FuncionarioViewSet
from apps.item_adicional.views import ItemAdicionalViewSet
from apps.manutencao.views import ManutencaoViewSet
from apps.multa.views import MultaViewSet
from apps.pagamento.views import PagamentoViewSet
from apps.reserva.views import ReservaViewSet
from apps.seguro.views import SeguroViewSet
from apps.veiculo.views import VeiculoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'carteiras-motorista', CarteiraMotoristaViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'agencias', AgenciaViewSet)
router.register(r'categorias-veiculo', CategoriaVeiculoViewSet)
router.register(r'veiculos', VeiculoViewSet)
router.register(r'adicionais', AdicionalViewSet)
router.register(r'seguros', SeguroViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'itens-adicionais', ItemAdicionalViewSet)
router.register(r'manutencoes', ManutencaoViewSet)
router.register(r'multas', MultaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('apps.pessoa.urls')),
    path('adicionais/', include('apps.adicional.urls')),
    path('clientes/', include('apps.cliente.urls')),
    path('carteiras/', include('apps.carteira_motorista.urls')),
    path('itens-adicionais/', include('apps.item_adicional.urls')),
    path('multas/', include('apps.multa.urls')),
    path('seguros/', include('apps.seguro.urls')),
    path('pessoas/', include('apps.pessoa.urls')),
    path('agencias/', include('apps.agencia.urls')),
    path('categorias-veiculo/', include('apps.categoria_veiculo.urls')),
    path('veiculos/', include('apps.veiculo.urls')),
    path('funcionarios/', include('apps.funcionario.urls')),
    path('reservas/', include('apps.reserva.urls')),
    path('pagamentos/', include('apps.pagamento.urls')),
    path('manutencoes/', include('apps.manutencao.urls')),
]
