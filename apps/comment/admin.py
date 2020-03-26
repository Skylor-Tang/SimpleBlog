from django.contrib import admin

# Register your models here.

from apps.comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'nickname', 'content', 'website', 'add_time']