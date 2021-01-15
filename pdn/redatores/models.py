from django.db import models
from filebrowser.fields import FileBrowseField


class Redator(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    decricao = models.TextField()
    foto = FileBrowseField("Image", max_length=200, directory="static/img/", extensions=[".jpg"], blank=True)
    
    def __str__(self):
        return self.nome