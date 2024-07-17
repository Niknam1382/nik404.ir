from django.shortcuts import render, get_object_or_404, HttpResponse
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm

# Create your views here.
def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)

    posts = Paginator(posts, 4)
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger :
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog.html', context)

def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
    now = timezone.now()
    posts = Post.objects.filter(status=True).exclude(published_date__gt=now)
    post = get_object_or_404(posts, pk=pid)
    form = CommentForm()
    context = {'post': post}
    return render(request, 'blog-details.html', context)

def blog_category(request, cat):
    now = timezone.now()
    posts = Post.objects.filter(status=True, category__name=cat).order_by('-published_date').exclude(published_date__gt=now)
    context = {'posts': posts}
    return render(request, 'blog.html', context)

def blog_author(request, author):
    now = timezone.now()
    posts = Post.objects.filter(status=True, author__username=author).order_by('-published_date').exclude(published_date__gt=now)
    context = {'posts': posts}
    return render(request, 'blog.html', context)

def blog_search(request):
    now = timezone.now()
    posts = Post.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog.html', context)