from django.urls import path
# from clientes.views import clientes
# from clientes.views import clientes
from clientes.views import clientes

urlpatterns = [
    path('', clientes.mostrar, name='clientes_mostrar'),
    path('agregar', clientes.agregar, name='clientes_agregar'),
    path('editar/<int:id_cliente>', clientes.editar, name='clientes_editar'),
    path('eliminar/<int:id_cliente>', clientes.eliminar, name='clientes_eliminar'),
]
