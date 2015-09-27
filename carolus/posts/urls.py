# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from .api import PostAPIView

router = DefaultRouter()
router.register(r'post', PostAPIView, base_name='post')


urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
)
