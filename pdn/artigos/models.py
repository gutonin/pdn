from django.db import models
from filebrowser.fields import FileBrowseField
from django.utils import timezone
from categorias.models import Categoria
from tags.models import Tag
from redatores.models import Redator
from tags.utils import slug_generator


class Artigo(models.Model):
    slug = models.SlugField(max_length=100, null=True, blank=True)
    chapeu = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    legenda = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(default=timezone.now, blank=True)
    imagem = FileBrowseField("Image", max_length=200, directory="static/img/", extensions=[".jpg",".png",], blank=True)
    texto = models.TextField(null=True, blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    redator = models.ForeignKey(Redator, null=True, blank=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.titulo)
        super(Artigo, self).save(*args, **kwargs)


