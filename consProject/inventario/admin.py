from django.contrib import admin
from inventario.models import Categoria, Producto

@admin.register(Categoria)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description')
    list_display_links = ('id', 'name')