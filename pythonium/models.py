from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from jdatetime import date
from jdatetime import datetime as jdatetime
from taggit.managers import TaggableManager
from django.core.validators import MinValueValidator, MaxValueValidator

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

class VideoFile(models.Model):
    videofile = models.FileField(upload_to='deploy/videos/%Y/%m/%d/', null=True, verbose_name="")
    slug = models.SlugField(unique=True)
    title= models.CharField(max_length=500)
    discription = models.TextField()
    season = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    
class Video(models.Model):
    slug = models.SlugField(unique=True)
    title= models.CharField(max_length=500)
    discription = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    # videofile= models.FileField(upload_to='deploy/videos/%Y/%m/%d/', null=True, verbose_name="")
    video = models.ManyToManyField(VideoFile)
    status = models.BooleanField(default=False)
    image = models.ImageField(default='images/default.jpg')
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    comment_counter = models.IntegerField(default=0)

    def shamsi_publish_date(self):
           return date.fromgregorian(date=self.published_date)
    
    def persian_published_date(self):
        month_number = jdatetime.fromgregorian(datetime=self.published_date).month
        return persian_month_names[month_number]

    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return reverse ("deploy:detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.title + ": " + str(self.id)
    
class Comment(models.Model):
    Video = models.ForeignKey(Video, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    stars = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])