from django.contrib import admin

from django.contrib import admin
from .models import Categoria, LugarPatrimonial

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']

class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion', 'anio_construccion', 'categoria']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(LugarPatrimonial, LugarPatrimonialAdmin)