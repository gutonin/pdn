from django.db import models
from tags.utils import slug_generator


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    exibir_categoria = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.nome)
        super(Categoria,self).save(*args, **kwargs)
    