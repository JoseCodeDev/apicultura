from django.urls import path
# from almacen_productos import views
from almacen_productos.views import categorias, productos

urlpatterns = [
    path('categorias/', categorias.mostrar, name='mostrar_categorias'),
    path('categorias/agregar', categorias.agregars, name='agregar_categorias'),
    path('categorias/editar/<int:id_categoria>', categorias.editar, name='editar_categorias'),
    path('categorias/eliminar/<int:id_categoria>', categorias.eliminar, name='eliminar_categorias'),
    path('productos/', productos.mostrar, name='productos_mostrar'),
    path('productos/agregar', productos.agregar, name='productos_agregar'),
    path('productos/editar/<int:id_producto>', productos.editar, name='productos_editar'),
    path('productos/eliminar/<int:id_producto>', productos.eliminar, name='productos_eliminar'),
]
