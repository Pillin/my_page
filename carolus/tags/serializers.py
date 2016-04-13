#-*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    """
    Serializador de posts
    """

    class Meta:
        model = Tag
