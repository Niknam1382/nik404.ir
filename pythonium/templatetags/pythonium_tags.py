from django import template
from pythonium.models import Video, VideoFile
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