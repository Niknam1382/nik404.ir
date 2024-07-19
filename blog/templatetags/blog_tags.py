from django import template
from blog.models import Post, Category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/categories.html')
def post_categories():
    now = timezone.now()
    posts = Post.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories :
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('blog/recent.html')
def recent():
    now = timezone.now()
    posts = Post.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)[:3]
    return {'posts': posts}

@register.inclusion_tag('blog/tags.html')
def tags():
    now = timezone.now()
    posts = Post.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)
    tags = []
    for post in posts:
        tags.extend(post.tags.all())
    unique_tags = list(set(tags))
    return {'tags': unique_tags}