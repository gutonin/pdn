from django.shortcuts import render
from .models import Artigo

# Create your views here.
def home(request):
    template = 'index.html'
    principal = Artigo.objects.order_by('-data_publicacao').only()
    context = {'principal': principal}
    return render(request, template, context)

def materia(request, categoria=None, artigo=None):
    template = 'materia.html'
    artigo = Artigo.objects.get(slug=artigo)
    context = {'artigo':artigo}
    return render(request, template, context)
