from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import strip_tags

from DjangoUeditor.models import UEditorField

from apps.users.models import BaseModel
from apps.users.models import BaseModel


UserProfile = get_user_model()


class Category(BaseModel):
    STATUS_ITEMS = (
        ('1', '正常'),
        ('0', '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.CharField(max_length=1, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(UserProfile, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    # 设置模型的返回值
    def __str__(self):
        return self.name


class Tag(BaseModel):
    STATUS_ITEMS = (
        ('1', '正常'),
        ('0', '删除'),
    )

    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.CharField(max_length=1, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(UserProfile, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = '标签'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Post(BaseModel):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name="标题")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = UEditorField(verbose_name="正文", width=600, height=300, imagePath="post/ueditor/images/",
                          filePath="post/ueditor/files/", default="")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    owner = models.ForeignKey(UserProfile, verbose_name="作者", on_delete=models.CASCADE)

    # 新增 views 字段记录阅读量
    views = models.PositiveIntegerField(default=0, verbose_name="阅读量")
    # 新增 comments 评论量

    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)

    # def get_absolute_url(self):
    #     return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-add_time', 'title']

    def __str__(self):
        return self.title

    # def increase_views(self):
    #     self.views += 1
    #     self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 如果没有填写摘要，摘取前54个字符
        if not self.desc:
            self.desc = strip_tags(self.content)[:54]+'...'
        super().save(*args, **kwargs)
