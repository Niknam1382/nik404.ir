from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "published_date"                           # Time Filter
    empty_value_display = "-empty-"
    list_display = ["title", "status", "counted_views",]
    list_filter = ['status', ]
    #ordering = ["created_date"]
    search_fields = ["title", "content", ]
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    empty_value_display = "-empty-"
    list_display = ['created_at', 'name', 'email', 'approved']
    list_filter = ['approved', ]
    search_fields = ["email", "message", 'name', 'post']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)