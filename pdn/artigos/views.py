from django.shortcuts import render
from .models import Artigo
from categorias.models import Categoria

# Create your views here.
def home(request):
    template = 'index.html'
    principal = Artigo.objects.order_by('-data_publicacao').only()
    categorias = Categoria.objects.all().only()
    context = {'principal': principal, 'categorias':categorias}
    return render(request, template, context)

def materia(request, categoria=None, artigo=None):
    template = 'materia.html'
    artigo = Artigo.objects.get(slug=artigo)
    context = {'artigo':artigo}
    return render(request, template, context)

def categoria(request, categoria=None):
    template = 'listagem.html'
    print(categoria)
    artigos = Artigo.objects.filter(categoria__slug=categoria)
    context = {'artigos': artigos}
    print(artigos)
    return render(request, template, context)
