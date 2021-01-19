from django.db import models
from .utils import slug_generator


class Tag(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.nome, self.slug)
    
    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.nome)
        super(Tag, self).save(*args, **kwargs)
