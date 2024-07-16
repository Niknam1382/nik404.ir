from django.urls import path
from website.views import test_view, index_view

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('test', test_view),
]