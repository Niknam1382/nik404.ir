from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
    path('reset', reset_password, name='reset1'),
    path('reset-password',reset_password_view , name='reset2'),
    path('panel',upload_profile_picture, name='panel'),
    path('active', active_item, name='active'),
]