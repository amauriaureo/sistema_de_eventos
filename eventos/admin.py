from django.contrib import admin

from eventos.models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
