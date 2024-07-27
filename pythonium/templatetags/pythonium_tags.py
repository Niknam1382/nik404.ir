from django import template
from pythonium.models import Video, VideoFile, Category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('pythonium/videos.html')
def pythonium_videos():
    now = timezone.now()
    videos = Video.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    videofile = VideoFile.objects.all()
    video_dict = {}
    for i in videofile:
        video_dict[i] = videos.filter(videos=i)
    return {'videos':video_dict}

@register.inclusion_tag('pythonium/categories.html')
def post_categories():
    now = timezone.now()
    videos = Video.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories :
        cat_dict[name] = videos.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('pythonium/tags.html')
def tags():
    now = timezone.now()
    videos = Video.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    tags = []
    for post in videos:
        tags.extend(post.tags.all())
    unique_tags = list(set(tags))
    return {'tags': unique_tags}

@register.inclusion_tag('pythonium/recent.html')
def recent():
    now = timezone.now()
    videos = Video.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)[:3]
    return {'videos': videos}