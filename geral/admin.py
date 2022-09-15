from django.contrib import admin
from .models import Categoria, Pagina, Autor


class PaginaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data', 'categorias', 'autor']
    search_fields = ['categorias', 'autor', 'titulo']


admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Pagina, PaginaAdmin)
