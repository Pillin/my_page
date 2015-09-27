#-*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    """
    Serializador de posts
    """

    class Meta:
        model = Post
