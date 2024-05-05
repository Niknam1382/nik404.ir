from django.db import models
from django.contrib.auth.models import User
from jdatetime import date

MONTHS_FA = {
    'Farvardin': 'فروردین',
    'Ordibehesht': 'اردیبهشت',
    'Khordad': 'خرداد',
    'Tir': 'تیر',
    'Mordad': 'مرداد',
    'Shahrivar': 'شهریور',
    'Mehr': 'مهر',
    'Aban': 'آبان',
    'Azar': 'آذر',
    'Dey': 'دی',
    'Bahman': 'بهمن',
    'Esfand': 'اسفند'
}


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model) :
    image = models.ImageField(upload_to='blog', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.id)
    
    def shamsi_publish_date(self):
        shamsi_date = date.fromgregorian(date=self.published_at)
        month_fa = MONTHS_FA[shamsi_date.strftime('%B')]
        return f"{shamsi_date.day} {month_fa}"
    
    def shamsi_publish_day(self):
        shamsi_date = date.fromgregorian(date=self.published_at)
        return f"{shamsi_date.day}"
    
    def shamsi_publish_mounth(self):
        shamsi_date = date.fromgregorian(date=self.published_at)
        month_fa = MONTHS_FA[shamsi_date.strftime('%B')]
        return f"{month_fa}"
    
    class Meta:
        ordering = ('-created_at',)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name+' '+self.last_name