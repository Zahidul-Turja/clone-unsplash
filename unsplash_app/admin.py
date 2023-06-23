from django.contrib import admin

from .models import User, Post, Tag

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "user_name", "email", "password")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
