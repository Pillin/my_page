# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .serializers import PostSerializer
from .models import Post


class PostAPIView(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset
