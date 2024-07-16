from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=True)
    context = {'posts': posts}
    return render(request, 'blog.html', context)

def blog_single(request, pid):
    #post = Post.objects.get(id=pid)
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    return render(request, 'blog-details.html', context)

def blog_category(request, cat):
    posts = Post.objects.filter(status=True, category__name=cat)
    context = {'posts': posts}
    return render(request, 'blog.html', context)