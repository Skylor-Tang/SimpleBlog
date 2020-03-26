from django.shortcuts import render, reverse, redirect
from django.views.generic import View

from apps.blog.models import Post
from apps.comment.models import Comment
from apps.comment.forms import CommentForm


class CommentView(View):
    def post(self, request, post_id, *args, **kwargs):
        post = Post.objects.get(id=int(post_id))
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            url = reverse('blog:post_detail', kwargs={'pk': post_id})
            return redirect(url)
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': comment_form,
                       'comment_list': comment_list
                       }
            return render(request, 'single.html', context=context)

