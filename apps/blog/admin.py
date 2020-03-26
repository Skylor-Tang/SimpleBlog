from django.contrib import admin

# Register your models here.

from apps.blog.models import Category, Tag, Post
from django.utils.html import format_html

from django.contrib.admin.models import LogEntry


# class PostInline(admin.TabularInline):   # 还有StackedInline样式
#     '''
#     在同一页面编辑关联数据，这要求关联的页面中要有本类型作为外键
#     '''
#     fields = ('title','desc','owner')
#     extra = 1  # 控制额外多几个
#     model = Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # inlines = [PostInline, ]
    list_display = ['name', 'status', 'is_nav', 'add_time', 'post_count']
    # fields = ['name', 'status', 'is_nav']

    # 当前分类型的文章数
    def post_count(self, obj):
        return obj.post_set.count()

    # 指定表头字段的显示
    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'add_time']
    # fields = ['name', 'status']


class CategoryOwnerFilter(admin.SimpleListFilter):
    """
    自定义过滤器只展示当前用户的分类
    """
    title = "分类过滤器"     # 过滤器 以 xx 的名字
    parameter_name = 'owner_category'   # http://127.0.0.1:8000/admin/blog/post/?owner_category=1   1 2 是查表返回的ID值

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name' ) # 只能接受两个参数 其中id 用于上面的用处 相当于编号 后面的值则是展示的值

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'status', 'views',
        'add_time', 'owner',
    ]


# @admin.register(LogEntry)
# class LogEntryAdmin(admin.ModelAdmin):
#     list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']