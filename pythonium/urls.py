from django.urls import path
from pythonium.views import pythonium_view, pythonium_single, pythonium_search, video_player

app_name = 'pythonium'

urlpatterns = [
    path('', pythonium_view, name='pythonium'),
    path('<int:vid>', pythonium_single, name='single'),
    path('search/', pythonium_search, name='search'),
    path('video/<int:video_id>/', video_player, name='video_player'),
    path('<str:cat>', pythonium_view, name='category'),
    path('author/<str:author>', pythonium_view, name='author'),
    path('tag/<str:tag_name>', pythonium_view, name='tag' )
]