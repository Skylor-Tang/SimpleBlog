# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 17:46
# @Author  : Skylor Tang
# @Email   : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from apps.blog.views import IndexView, PostDetailView, ArchivesView, CategoryView, TagView

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<cate_id>[0-9]+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', TagView.as_view(), name='tag'),
    # url(r'^search/$', views.search, name='search'),
]