from django.contrib import admin
from website.models import content
# Register your models here.

class contentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"                           # Time Filter
    empty_value_display = "-empty-"
    list_display = ["subject", "name", "email",]
    search_fields = ["subject", "message", ]
    list_filter = ["email"]

admin.site.register(content, contentAdmin)