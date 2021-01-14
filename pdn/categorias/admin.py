from django.contrib import admin
from .models import Tag

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    model = Tag
    fields = ('nome','slug')
    readonly_fields = ('slug',)


admin.site.register(Tag, TagAdmin)