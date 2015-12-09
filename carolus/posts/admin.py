# -*- coding: utf-8 -*-
from django.contrib import admin
from posts.models import Post
from posts.forms import PostAdminForm


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
