# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify


class Tag(MPTTModel):
    tag_id = models.IntegerField(
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=100,
        verbose_name=u'Nombre'
    )
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        verbose_name=u'Categoría padre'
    )
    slug = models.SlugField()
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Orden'
    )

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['order', 'name']

    class Meta:
        verbose_name = u'Categoría'
        unique_together = ('parent', 'slug')

    def save(self, *args, **kwargs):
        """
        Sobreescrito para generar el slug
        """
        if not self.id:
            self.slug = slugify(self.name, max_length=50)

        super(Tag, self).save(*args, **kwargs)
