from django.urls import path
from website.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]