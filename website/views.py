from django.shortcuts import render

app_name = 'website'
# Create your views here.
def index_view(request) :
    return render(request, 'index-2.html')