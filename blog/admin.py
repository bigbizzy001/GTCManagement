from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'body', 'publish')
    list_filter = ('title', 'body', 'publish')
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'


# admin.site.register(Post, PostAdmin)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'active', 'created')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


