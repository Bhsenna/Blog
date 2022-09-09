from django.contrib import admin
from .models import Categoria, Pagina, Autor
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Pagina)
