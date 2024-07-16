from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(default='images/default.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(default=False)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    '''
    tag
    '''
    def __str__(self):
        return '{} - {}'.format(self.id, self.title)
    
    class Meta:
        ordering = ["created_date"]