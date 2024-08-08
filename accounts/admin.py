from django.contrib import admin
from accounts.models import profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(profile, ProfileAdmin)
