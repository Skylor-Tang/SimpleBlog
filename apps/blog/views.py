from django.shortcuts import render
from django.views.generic import View, ListView

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.blog.models import Category, Post, Tag
from apps.comment.forms import CommentForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        all_posts = Post.objects.all()
        # 最新文章
        latest_article = all_posts.order_by('-add_time')[:3]

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_posts, per_page=3, request=request)
        all_posts = p.page(page)

        return render(request, "index.html", {
            "all_posts": all_posts,
            "latest_article": latest_article,

        })


class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=int(pk))
        post.views += 1
        post.save()
        comment_list = post.comment_set.all()
        return render(request, "single.html", {
            "post": post,
            'comment_list': comment_list,
        })


class ArchivesView(View):
    def get(self, request, year, month, *args, **kwargs):
        # year = self.kwargs.get('year')
        # month = self.kwargs.get('month')
        all_posts = Post.objects.filter(add_time__year=int(year), add_time__month=int(month))
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_posts, per_page=3, request=request)
        all_posts = p.page(page)

        return render(request, "index.html", {
            "all_posts": all_posts,
        })


class CategoryView(View):
    def get(self, request, cate_id, *args, **kwargs):
        all_posts = Post.objects.filter(category=int(cate_id))
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_posts, per_page=3, request=request)
        all_posts = p.page(page)

        return render(request, "index.html", {
            "all_posts": all_posts,
        })


class TagView(View):
    def get(self, request, tag_id, *args, **kwargs):
        all_posts = Post.objects.filter(tag=int(tag_id))
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_posts, per_page=3, request=request)
        all_posts = p.page(page)

        return render(request, "index.html", {
            "all_posts": all_posts,
        })



