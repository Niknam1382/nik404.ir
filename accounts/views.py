from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'accounts/sign-up.html')