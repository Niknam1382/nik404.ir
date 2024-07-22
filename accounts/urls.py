from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login', login, name='login'),
    #path('logout', logout, name='logout'),
    #path('signup', signup, name='signup'),
]