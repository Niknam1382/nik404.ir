from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"                           # Time Filter
    empty_value_display = "-empty-"
    list_display = ["title", "status", "counted_views",]
    list_filter = ['status', ]
    #ordering = ["created_date"]
    search_fields = ["title", "content", ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)