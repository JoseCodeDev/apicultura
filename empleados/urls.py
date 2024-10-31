from django.urls import path
from empleados.views import departamentos, puestos, empleados

urlpatterns = [
    path('', empleados.mostrar, name='empleados_mostrar'),
    path('agregar', empleados.agregar, name='empleados_agregar'),
    path('editar/<int:id_cliente>', empleados.editar, name='empleados_editar'),
    path('eliminar/<int:id_cliente>', empleados.eliminar, name='empleados_eliminar'),
    
    path('departamentos/', departamentos.mostrar, name='departamentos_mostrar'),
    path('departamentos/agregar', departamentos.agregar, name='departamentos_agregar'),
    path('departamentos/editar/<int:id_departamento>', departamentos.editar, name='departamentos_editar'),
    path('departamentos/eliminar/<int:id_departamento>', departamentos.eliminar, name='departamentos_eliminar'),
    
    path('puestos/', puestos.mostrar, name='puestos_mostrar'),
    path('puestos/agregar', puestos.agregar, name='puestos_agregar'),
    path('puestos/editar/<int:id_puesto>', puestos.editar, name='puestos_editar'),
    path('puestos/eliminar/<int:id_puesto>', puestos.eliminar, name='puestos_eliminar'),
]
