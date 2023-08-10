from django.db import models


class Categoria(models.Model):

    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', blank=True)
