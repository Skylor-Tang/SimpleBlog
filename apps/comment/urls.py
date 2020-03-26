# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 17:46
# @Author  : Skylor Tang
# @Email   : 
# @File    : urls.py
# @Software: PyCharm


from django.conf.urls import url

from apps.comment.views import CommentView

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_id>[0-9]+)/$', CommentView.as_view(), name='post_comment'),
]