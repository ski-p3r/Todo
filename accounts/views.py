from django.shortcuts import render, redirect
from .models import Account, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        first_name  = request.POST['first_name']
        last_name   = request.POST['last_name']
        email       = request.POST['email']
        password    = request.POST['password']

        user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    
    return render(request, 'register.html')

def sign_in(request):
    if request.method == 'POST':
        email       = request.POST['email']
        password    = request.POST['password']

        user = authenticate(request,email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
    return render(request, 'login.html')

@login_required(login_url = 'sign_in')
def sign_out(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('sign_in')

@login_required(login_url = 'sign_in')
def dashboard(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        context = {
            'profile': profile,
            'user': user,
        }
    except:
        context = {
            'user': user,
        }
    return render(request, 'dashboard.html', context)

@login_required(login_url = 'sign_in')
def change_password(request):
    p=request.user
    t = p.password
    y=Account.objects.get(email=p)
    if request.method == 'POST':
        password1   = request.POST['password1']
        password    = request.POST['password']
        f = check_password(password1,t)
        if f:
            y.set_password(password)
            y.save()
            return redirect('dashboard')
        else:
            pass
    try:
        profile = Profile.objects.get(user=y)
        context = {
            'profile': profile,
        }   
    except:
        context = {}
    
    return render(request, 'change_Password.html', context)

@login_required(login_url = 'sign_in')
def acc_set(request):  
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        context = {
            'profile': profile,
            'user': user,
        }
    except:
        context = {
            'user': user,
        }
    return render(request, 'account_setting.html', context)


@login_required(login_url = 'sign_in')
def acc_del(request):
    p=request.user
    y=Account.objects.get(email=p)
    y.delete()
    return redirect('sign_up')

@login_required(login_url = 'sign_in')
def edit_acc(request):
    user = request.user
    if request.method == 'POST':
        first_name  = request.POST['first_name']
        last_name   = request.POST['last_name']
        email       = request.POST['email']

        users = Account.objects.get(email=user)
        users.first_name  = first_name
        users.last_name   = last_name
        users.email       = email
        users.is_active = True
        users.save()
        return redirect('dashboard')
    try:
        profile = Profile.objects.get(user=user)
        context = {
            'profile': profile,
            'user': user,
        }
    except:
        context = {
            'user': user,
        }
    return render(request, 'edit_account.html', context)

@login_required(login_url = 'sign_in')
def profile_pic(request):
    y=request.user
    if request.method == 'POST':
        img = request.FILES['image']
        try:
            user = Profile.objects.get(user=y)
            user.product_img = img
            user.save()
            return redirect('dashboard')
        except:
            user = Profile.objects.create(user=y,product_img=img)
            user.save()
            return redirect('dashboard')
    try:
        profile = Profile.objects.get(user=y)
        context = {
            'profile': profile,
            'user': y,
        }
    except:
        context = {
            'user': y,
        }
    return render(request, 'profile_pic.html', context)



# @login_required(login_url = 'sign_in')