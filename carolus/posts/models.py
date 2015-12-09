# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=3000,
        verbose_name=u'Descripción'
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u'Fecha de creación'
    )

    def __unicode__(self):
        return str(self.title)

    class Meta:
        ordering = ["creation_date"]
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'
