from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('post-<int:pid>', blog_single, name='single'),
    path('<str:cat>', blog_category, name='category'),
]