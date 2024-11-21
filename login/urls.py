from django.urls import path
from .views import iniciar_sesion, crerrar_sesion

urlpatterns = [
    path('', iniciar_sesion, name='login'),
    path('logout/', crerrar_sesion, name='logout'),
]
