from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='profile', default='images/default.jpg')

    def __str__(self):
        return self.user.username