from django.contrib import admin
from pythonium.models import Video, Category, VideoFile, python_comment, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class videoAdmin(SummernoteModelAdmin):
    summernote_fields = ('discription',)
class CategoryAdmin(admin.ModelAdmin):
    pass
class VideoFileAdmin(admin.ModelAdmin):
    pass
class python_commentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video, videoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(VideoFile, VideoFileAdmin)
admin.site.register(python_comment, python_commentAdmin)
admin.site.register(Comment)


# class PostAdmin(SummernoteModelAdmin):
#     date_hierarchy = "published_date"                           # Time Filter
#     empty_value_display = "-empty-"
#     list_display = ["title", "status", "counted_views",]
#     list_filter = ['status', ]
#     #ordering = ["created_date"]
#     search_fields = ["title", "content", ]
#     summernote_fields = ('content',)
