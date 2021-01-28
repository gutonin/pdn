from django.shortcuts import render
from .models import Artigo
from categorias.models import Categoria
from redatores.models import Redator

# Create your views here.
def home(request):
    template = 'index.html'
    principal = Artigo.objects.order_by('-data_publicacao')
    categorias = Categoria.objects.all()
    context = {'principal': principal, 'categorias':categorias}
    return render(request, template, context)

def materia(request, categoria=None, artigo=None):
    template = 'materia.html'
    artigos = Artigo.objects.get(slug=artigo)
    context = {'artigos': artigos}
    return render(request, template, context)

def categoria(request, categoria=None):
    template = 'listagem.html'
    cat = Categoria.objects.get(slug=categoria)
    artigos = Artigo.objects.filter(categoria__slug=categoria)
    context = {'artigos': artigos, 'categoria': cat}
    return render(request, template, context)
