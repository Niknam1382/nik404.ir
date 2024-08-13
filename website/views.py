from django.shortcuts import render, redirect
from website.forms import ContentForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from website.models import w1, w2e
from blog.models import Post
from django.utils import timezone

# Create your views here.
def test_view(request):
    return render(request, 'test.html')

def index_view(request):
    w11 = w1.objects.all()[0]
    w22 = w2e.objects.all()[0]
    now = timezone.now()
    posts = Post.objects.filter(status=True).order_by('-published_date').exclude(published_date__gt=now)[:3]
    return render(request, 'index.html', {'w1': w11, 'w2': w22, 'posts': posts})

def about_view(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = f'name = {name}\n phone = {phone}\n email = {email}\n\nmessage:\n{form.cleaned_data['message']}'
            messages.add_message(request, messages.SUCCESS, f"پیام شما ارسال شد")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['niknam151412@gmail.com', 'niksky404@gmail.com']
            send_mail( subject, message, email_from, recipient_list )
            return redirect('/about')
        else:
            messages.add_message(request, messages.WARNING, f"پیام شما ارسال نشد")
    form = ContentForm()
    return render(request, 'sub-pages/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = f'name = {name}\n email = {email}\n\nmessage:\n{form.cleaned_data['message']}'
            messages.add_message(request, messages.SUCCESS, f"پیام شما ارسال شد")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['niknam151412@gmail.com', 'niksky404@gmail.com']
            send_mail( 'فرم تماس سایت', message, email_from, recipient_list )
            print('----------------------------------------------------------------')
            return redirect('/')
        else:
            messages.add_message(request, messages.WARNING, f"پیام شما ارسال نشد")
    form = ContactForm()
    return render(request, 'sub-pages/contact.html')


def error_404(request, exception):
    return render(request, 'error/404.html', status=404)
 
def error_500(request):
    return render(request, 'error/500.html', status=500)

def error_403(request, exception):
    return render(request, 'error/403.html', status=403)