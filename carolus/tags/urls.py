# -*- coding: utf-8 -*-
from carolus.urls import router
from .api import TagAPIView

router.register(r'tag', TagAPIView, base_name='tag')
