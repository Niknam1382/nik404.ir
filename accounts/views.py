from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import re
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import django.contrib.auth
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
import random
from django.contrib.auth.models import User
# from accounts.models import CustomUser
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated == False :
            pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
            username = request.POST["username"]
            password = request.POST["password"]
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                # or password = form.cleaned_data.get()"password")
            if re.match(pattern, username):
                email = username
                if User.objects.filter(email=email).first() is not None:
                    user = User.objects.filter(email=email).first()
                else:
                    if usermail[0].islower():
                        usermail = usermail.capitalize()
                    else:
                        usermail = usermail.lower()
                    user = User.objects.filter(email=email).first()
            else:
                user = authenticate(username=username, password=password)
                if user == None:
                    if username[0].islower():
                        username = username.capitalize()
                    else:
                        username = username.lower()
                    user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f"{request.user.first_name} با موفقیت به سیستم وارد شدید")
                # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))                
                now = datetime.now()
                formatted_date = now.strftime("%H:%M")
                subject = 'ورود به حساب کاربری'
                message = f'{request.user.first_name} شما در ساعت {formatted_date} به حساب کاربری خود وارد شدید.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.user.email, ]
                send_mail( subject, message, email_from, recipient_list )
                return redirect('/')
            else:
                messages.add_message(request, messages.WARNING, "نام کاربری یا رمز عبور اشتباه!")
                return redirect('/accounts/login')
        else :
            messages.add_message(request, messages.INFO, f"{request.user.first_name} عزیز. شما قبلاََ به سیستم وارد شدید.")
            return redirect('/')
    form = AuthenticationForm
    return render(request, 'accounts/login.html', {"form": form})

@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            User = django.contrib.auth.get_user_model()
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone = request.POST['phone']
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if password1 == password2:
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
                        user.is_superuser = False
                        user.is_staff = False
                        user.phone_number = phone
                        user.save()
                        messages.add_message(request, messages.SUCCESS, 'حساب کاربری شما با موفقیت ایجاد شد.')
                        subject = 'ساخت حساب کاربری'
                        message = f'{request.user.first_name} {request.user.last_name} عزیز . حساب کاربری شما با موفقیت ساخته شد . نام کاربری شما {request.user.username}'
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [request.user.email, ]
                        send_mail( subject, message, email_from, recipient_list )
                        return redirect('/')
                    else:
                        messages.add_message(request, messages.WARNING, f"گذرواژه ها مطابقت ندارند")
                else:
                    messages.add_message(request, messages.WARNING, 'این ایمیل در سیستم موجود است و نمی‌توانید از آن استفاده کنید')
            else:
                messages.add_message(request, messages.WARNING, 'این نام کاربری ثبت شده. لطفا نام کاربری جدیدی را امتحان کنید.')
    return render(request, 'accounts/signup.html')

def reset_password(request):
    if request.method == 'POST':
        usermail = request.POST['usermail']
        x = random.randint(100000, 999999)
        regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        if(re.search(regex,usermail)):
            if User.objects.filter(email=usermail).first() is not None:
                user = User.objects.filter(email=usermail).first()
                email = usermail
            else:
                if usermail[0].islower():
                    usermail = usermail.capitalize()
                else:
                    usermail = usermail.lower()
                user = User.objects.filter(email=usermail).first()
        else:
            user = User.objects.get(username=usermail)
        email = user.email
        subject = f'کد بازیابی {x}'
        message = f'کد بازیابی رمز عبور حساب شما : {x}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

        request.session['username'] = usermail
        request.session['code'] = x
        return redirect('/accounts/reset-password')
    return render(request, 'accounts/reset1.html')

def reset_password_view(request):
    # User = django.contrib.auth.get_user_model()
    if request.method == 'POST':
        usermail = request.session['username']
        code = request.session['code']
        regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        print(usermail,code)
        if(re.search(regex,usermail)):
            print('eeee')
            if User.objects.filter(email=usermail).first() is not None:
                user = User.objects.filter(email=usermail).first()
                email = usermail
            else:
                if usermail[0].islower():
                    usermail = usermail.capitalize()
                else:
                    usermail = usermail.lower()
                user = User.objects.filter(email=usermail).first()
        else:
            user = User.objects.get(username=usermail)
        email = user.email
        print(user)
        confirm = request.POST['confirm']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if int(confirm) == code:
            if pass1 == pass2:
                user.set_password(pass1)
                messages.add_message(request, messages.SUCCESS, f"رمز عبور شما با موفقیت تغییر کرد")
                subject = 'تغییر رمز عبور'
                message = f'{user.first_name} {user.last_name} عزیز. رمز عبور شما با موفقیت تغییر یافت.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )
                return redirect('/accounts/login')
            else:
                messages.add_message(request, messages.WARNING, f"گذرواژه ها مطابقت ندارند")
                return redirect('/accounts/reset')
        else:
            messages.add_message(request, messages.WARNING, f"کد تایید صحیح نمیباشد")
            return redirect('/accounts/reset')
    return render(request, 'accounts/reset2.html')