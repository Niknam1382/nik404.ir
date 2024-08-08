from django.db import models
from django.contrib.auth.models import User
from pythonium.models import Video

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='profile_pics/', default='images/default.jpg')
    phone = models.CharField(max_length=255, null=True, blank=True)
    videos = models.ManyToManyField(Video)