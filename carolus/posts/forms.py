# -*- coding: utf-8 -*-
from django import forms
from ckeditor.widgets import CKEditorWidget
from posts.models import Post


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    description_en = forms.CharField(widget=CKEditorWidget())
    description_es = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'
