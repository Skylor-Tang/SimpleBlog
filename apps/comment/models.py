from django.db import models
from apps.blog.models import Post
from apps.users.models import BaseModel
# Create your models here.


class Comment(BaseModel):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="博客文章")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")

    class Meta:
        verbose_name = verbose_name_plural = "评论"
        ordering = ['-add_time']

    def __str__(self):
        return self.nickname