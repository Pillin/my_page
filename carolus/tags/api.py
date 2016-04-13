# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .serializers import TagSerializer
from .models import Tag


class TagAPIView(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    serializer_class = TagSerializer

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset
