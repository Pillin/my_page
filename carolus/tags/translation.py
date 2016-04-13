# -*- coding: utf-8 -*-
from modeltranslation.translator import register, TranslationOptions
from tags.models import Tag


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name', )
