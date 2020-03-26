# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 9:17
# @Author  : Skylor Tang
# @Email   : 
# @File    : blog_tags.py
# @Software: PyCharm

from django import template
from django.db.models.aggregates import Count

from ..models import Post, Category, Tag

register = template.Library()


@register.simple_tag
def get_recent_posts(num=3):
    return Post.objects.order_by('-add_time')[:num]


@register.simple_tag
def archives():
    '''
    归档
    '''
    return Post.objects.dates('add_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    '''
    分类
    '''
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    '''
    标签
    '''
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)



