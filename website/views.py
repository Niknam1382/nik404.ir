from django.shortcuts import render

app_name = 'website'
# Create your views here.
def index_view(request) :
    return render(request, 'index-2.html')

def about_view(request) :
    return render(request, 'about.html')

def service_view(request) :
    return render(request, 'service-solutions.html')

def contact_view(request) :
    return render(request, 'contact.html')