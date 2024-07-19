from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('post-<int:pid>', blog_single, name='single'),
    path('<str:cat>', blog_view, name='category'),
    path('author/<str:author>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path('tag/<str:tag_name>', blog_view, name='tag' )
]