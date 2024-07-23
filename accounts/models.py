from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     date_joined = models.DateField(auto_now_add=True)
#     last_login = models.DateField(auto_now=True)
#     address = models.TextField(null=True, blank=True)

#     # تغییر نام دسترسی‌های معکوس
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_groups',  # تغییر نام این دسترسی‌ها
#         blank=True,
#         help_text='The groups this user belongs to.',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_permissions',  # تغییر نام این دسترسی‌ها
#         blank=True,
#         help_text='Specific permissions for this user.',
#     )

#     def __str__(self):
#         return self.username
