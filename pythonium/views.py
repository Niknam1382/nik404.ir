from django.shortcuts import render, get_object_or_404
from pythonium.models import Video, VideoFile
from django.utils import timezone

# Create your views here.
def pythonium_view(request):
    now = timezone.now()
    videos = Video.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    context = {'videos': videos}
    return render(request, 'pythonium/pythonium.html', context)

def pythonium_single(request, vid):
    now = timezone.now()
    video = get_object_or_404(Video, id=vid)
    videos = Video.objects.filter(id=vid).order_by('-published_date').exclude(published_date__gt=now)
    seasons = video.video.values_list('season', flat=True).distinct()
    season_videos = {season: video.video.filter(season=season) for season in seasons}
    '''
    season_videos = {}
    for season in seasons:
        videos_in_season = video.video.filter(season=season)
        season_videos[season] = videos_in_season
    '''
    context = {'videos': videos, 'season_videos': season_videos}
    return render(request, 'pythonium/pythonium-single.html', context)


def pythonium_search(request):
    now = timezone.now()
    videos = Video.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            videos = videos.filter(discription__contains=s)
    context = {'videos': videos}
    return render(request, 'pythonium/pythonium.html', context)

def video_player(request, video_id):
    video_file = get_object_or_404(VideoFile, id=video_id)
    return render(request, 'pythonium/video_player.html', {'video_file': video_file})