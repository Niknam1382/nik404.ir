from django.db import models

# Create your models here.
class content(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.subject, self.name)
    
    class Meta:
        ordering = ["created_date"]