from django.urls import path
from almacen.views import categorias, productos, insumos

urlpatterns = [
    path('categorias/', categorias.mostrar, name='categorias_mostrar'),
    path('categorias/agregar', categorias.agregars, name='categorias_agregar'),
    path('categorias/editar/<int:id_categoria>', categorias.editar, name='categorias_editar'),
    path('categorias/eliminar/<int:id_categoria>', categorias.eliminar, name='categorias_eliminar'),
    
    path('productos/', productos.mostrar, name='productos_mostrar'),
    path('productos/agregar', productos.agregar, name='productos_agregar'),
    path('productos/editar/<int:id_producto>', productos.editar, name='productos_editar'),
    path('productos/eliminar/<int:id_producto>', productos.eliminar, name='productos_eliminar'),
    
    path('insumos/', insumos.mostrar, name='insumos_mostrar'),
    path('insumos/agregar', insumos.agregar, name='insumos_agregar'),
    path('insumos/editar/<int:id_insumo>', insumos.editar, name='insumos_editar'),
    path('insumos/eliminar/<int:id_insumo>', insumos.eliminar, name='insumos_eliminar'),
]
