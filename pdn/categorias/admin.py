from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    fields = ('nome','slug')
    readonly_fields = ('slug',)


admin.site.register(Categoria, CategoriaAdmin)
