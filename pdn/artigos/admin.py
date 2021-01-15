from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Artigo

# Register your models here.
class ArtigoModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Artigo, ArtigoModelAdmin)