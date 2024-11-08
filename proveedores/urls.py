from django.urls import path
from proveedores.views import proveedores

urlpatterns = [
    path('', proveedores.mostrar, name='proveedores_mostrar'),
    path('agregar', proveedores.agregar, name='proveedores_agregar'),
    path('editar/<int:id_proveedor>', proveedores.editar, name='proveedores_editar'),
    path('eliminar/<int:id_proveedor>', proveedores.eliminar, name='proveedores_eliminar'),
]
