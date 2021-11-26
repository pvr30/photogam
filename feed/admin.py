from django.contrib import admin
from django.db import models
from .models import Post, Comment, Like
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id', 'user')

class CommentModelAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('id', 'user', 'comment', 'post')

class LikeModelAdmin(admin.ModelAdmin):
    model = Like
    list_display = ('user', 'post')

admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Like, LikeModelAdmin)