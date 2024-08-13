from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5          # میزان اهمیت
    changefreq = "daily"    # زمان تغییرش

    def items(self):
        return ["website:index", "website:about", "website:contact"]

    def location(self, item):
        return reverse(item)