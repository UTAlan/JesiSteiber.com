from django.contrib import admin
from blog.models import Category, Tag, Post, Comment

class TagAdmin(admin.ModelAdmin):
    ordering = ('title',)

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'category', 'tags', 'groups', 'is_public')
    list_display = ('title', 'category', 'created_date', 'is_public')
    list_filter = ('category', 'groups', 'is_public')
    ordering = ('-created_date',)

admin.site.register(Category)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
