from django.contrib import admin
from apps.users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["username", "nick_name", "birthday", "gender", "address", "mobile"]

