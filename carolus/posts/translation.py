# -*- coding: utf-8 -*-
from modeltranslation.translator import register, TranslationOptions
from posts.models import Post


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
