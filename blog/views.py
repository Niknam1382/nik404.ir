from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.
def blog_view(request, **kwargs):
    
    now = timezone.now()
    posts = Post.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)

    if kwargs.get('cat') is not None:
        posts = posts.filter(status=True, category__name=kwargs['cat'])
    if kwargs.get('author') != None:
        posts = posts.filter(status=True, author__username=kwargs['author'])
    if kwargs.get('tag_name') :
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    
    posts = Paginator(posts, 4)
    try :
        if request.method == 'GET':
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
            parent_id = request.POST.get('parent_id')
            parent_comment = None
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
            new_comment = form.save(commit=False)
            new_comment.post = get_object_or_404(Post, pk=pid)
            new_comment.parent = parent_comment
            new_comment.save()
            messages.add_message(request, messages.INFO, "کامنت شما در صف بررسی قرار گرفت")
        else:
            messages.add_message(request, messages.INFO, "کامنت شما ثبت نشد. لطفا مجدداََ تلاش بفرمائید")
    now = timezone.now()
    posts = Post.objects.filter(status=True).exclude(published_date__gt=now)
    post = get_object_or_404(posts, pk=pid)
    post.counted_views += 1
    post.save()
    comments = Comment.objects.filter(approved=True, post=post.id, parent=None).order_by('created_at')
    comments_counter = comments.count()
    post.comment_counter = comments_counter
    post.save()
    form = CommentForm()
    context = {'post': post, 'form': form, 'comments': comments, 'comments_counter': comments_counter}
    return render(request, 'blog-details.html', context)
'''
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
'''
def blog_search(request):
    now = timezone.now()
    posts = Post.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog.html', context)