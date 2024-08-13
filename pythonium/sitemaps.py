from django.contrib.sitemaps import Sitemap
from pythonium.models import Video
from django.urls import reverse

class PythoniumSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Video.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self,item):
        return reverse('pythonium:single', kwargs={'vid':item.id})