from django.contrib import admin
from almacen_productos import models

# Register your models here.
@admin.register(models.Categoria)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('nombre',)
    ordering = ['id']


@admin.register(models.Producto)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock', 'categoria')
    search_fields = ('nombre', 'stock', 'categoria__nombre')
    list_filter = ('categoria',)
    ordering = ['id']