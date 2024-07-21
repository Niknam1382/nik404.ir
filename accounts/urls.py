from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('', test)
]