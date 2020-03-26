# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 21:16
# @Author  : Skylor Tang
# @Email   : 
# @File    : forms.py
# @Software: PyCharm


import re

from django import forms
from apps.comment.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']

