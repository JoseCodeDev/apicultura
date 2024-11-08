from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.mostrar, name='usuarios_mostrar'),
    path('agregar/', views.agregar, name='usuarios_agregar'),
    path('editar/<int:id_usuario>/', views.editar, name='usuarios_editar'),
    path('cambiarContrasenia/<int:id_usuario>/', views.cambiar_contrasenia, name='usuarios_cambiar_contrasenia'),
    path('eliminar/<int:id_usuario>/', views.eliminar, name='usuarios_eliminar'),
]
