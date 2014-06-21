# -*- coding: utf-8 -*-

from django.db import models


class Posts(models.Model):
    title = models.CharField('Título', max_length=100)
    publication_date = models.DateTimeField('Data de publicação', auto_now_add=True)
    content = models.TextField('Conteúdo')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __unicode__(self):
        return self.title