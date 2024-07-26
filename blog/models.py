from django.db import models
from django.contrib.auth.models import User
from jdatetime import date
from jdatetime import datetime as jdatetime
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager

persian_month_names = {
    1: 'فروردین',
    2: 'اردیبهشت',
    3: 'خرداد',
    4: 'تیر',
    5: 'مرداد',
    6: 'شهریور',
    7: 'مهر',
    8: 'آبان',
    9: 'آذر',
    10: 'دی',
    11: 'بهمن',
    12: 'اسفند',
}
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
    tags = TaggableManager()
    comment_counter = models.IntegerField(default=0)
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.title)
    
    def shamsi_publish_date(self):
           return date.fromgregorian(date=self.published_date)
    
    def persian_published_date(self):
        month_number = jdatetime.fromgregorian(datetime=self.published_date).month
        return persian_month_names[month_number]
    
    class Meta:
        ordering = ["-created_date"]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    stars = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'