from django.shortcuts import render, get_object_or_404
from pythonium.models import Video, VideoFile, python_comment, Comment
from django.utils import timezone
from pythonium.forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
# def pythonium_view(request):
#     now = timezone.now()
#     videos = Video.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
#     context = {'videos': videos}
#     return render(request, 'pythonium/pythonium.html', context)

def pythonium_view(request, **kwargs):
    now = timezone.now()
    videos = Video.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    if kwargs.get('cat') is not None:
        videos = videos.filter(status=True, category__name=kwargs['cat'])
    # if kwargs.get('author') != None:
    #     videos = videos.filter(status=True, author__username=kwargs['author'])
    if kwargs.get('tag_name') :
        videos = videos.filter(tags__name__in=[kwargs['tag_name']])
    videos = Paginator(videos, 9)
    try :
        if request.method == 'GET':
            page_number = request.GET.get('page')
            videos = videos.get_page(page_number)
    except PageNotAnInteger :
        videos = videos.get_page(1)
    except EmptyPage:
        videos = videos.get_page(1)
    context = {'videos': videos}
    return render(request, 'pythonium/pythonium.html', context)

def pythonium_single(request, vid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_id = request.POST.get('parent_id')
            parent_comment = None
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
            new_comment = form.save(commit=False)
            new_comment.Video = get_object_or_404(Video, pk=vid)
            new_comment.parent = parent_comment
            new_comment.save()
            messages.add_message(request, messages.INFO, "کامنت شما در صف بررسی قرار گرفت")
        else:
            messages.add_message(request, messages.INFO, "کامنت شما ثبت نشد. لطفا مجدداََ تلاش بفرمائید")
    now = timezone.now()
    video = get_object_or_404(Video, id=vid)
    video.counted_views += 1
    comments = Comment.objects.filter(approved=True, Video=video.id, parent=None).order_by('created_at')
    comments_counter = comments.count()
    videos = Video.objects.filter(id=vid).order_by('-published_date').exclude(published_date__gt=now)
    seasons = video.video.values_list('season', flat=True).distinct()
    season_videos = {season: video.video.filter(season=season) for season in seasons}
    '''
    season_videos = {}
    for season in seasons:
        videos_in_season = video.video.filter(season=season)
        season_videos[season] = videos_in_season
    '''
    
    context = {'videos': videos, 'season_videos': season_videos, 'video': video, 'comments_counter': comments_counter, 'comments': comments}
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
    if request.method == 'POST':
        pcm = python_comment.objects.create(user= request.user, message=request.POST.get('message'))
        pcm.save()
        messages.add_message(request, messages.INFO, 'کامنت شما ثبت شد')
    video_file = get_object_or_404(VideoFile, id=video_id)
    context = {'video_file': video_file}
    return render(request, 'pythonium/video_player.html', context)

def active_view(request, wid):
    user = User.objects.get(username=request.user.username)
    print(user)
    print(wid)
    return HttpResponse('no')