from django.urls import path
from pedidos_compras.views import pedidos

urlpatterns = [
    path('pedidos/', pedidos.mostrar, name='pedidos_mostrar'),
    path('pedidos/agregar/', pedidos.agregar, name='pedidos_agregar'),
    path('pedidos/editar/<int:id_pedido>/', pedidos.editar, name='pedidos_editar'),
    path('pedidos/eliminar/<int:id_pedido>/', pedidos.eliminar, name='pedidos_eliminar'),
]
