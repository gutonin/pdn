from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    fields = ('nome','slug','exibir_categoria')
    readonly_fields = ('slug',)
    list_display = ('nome','slug','exibir_categoria')


admin.site.register(Categoria, CategoriaAdmin)
