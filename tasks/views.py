from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from accounts.models import Account, Profile
from django.contrib import messages

# Create your views here.

def view_task(request, id):
    asd = Task.objects.get(id=id)
    context = {
        'task': asd,
    }
    return render(request, 'view.html', context)

@login_required(login_url = 'sign_in')
def my_task(request):
    asd = Task.objects.filter(author=request.user)
    context = {
        'task': asd,
    }
    return render(request, 'my_task.html', context)

@login_required(login_url = 'sign_in')
def create_task(request):
    y=request.user
    user = Account.objects.get(email=y)
    try:
        profile = Profile.objects.get(user=y)
    except:
        messages.error(request, 'Please add Profile Picture')
        return redirect('profile_pic')
    if request.method == 'POST':
        task = request.POST['task']
        description = request.POST['description']
        
        asd = Task.objects.create(profile=profile, author=user, task=task, description=description)
        asd.save()
        return redirect('home')
    return render(request, 'add.html')

@login_required(login_url = 'sign_in')
def edit_task(request, id):
    asd = Task.objects.get(author=request.user, id=id)
    if request.method == 'POST':
    
        task = request.POST.get('task')
        description = request.POST.get('description') 
        asd.task = task
        asd.description = description
        asd.save()
        return redirect('home')
    context = {
        'task': asd
    }
    return render(request, 'edit.html', context)

@login_required(login_url = 'sign_in')
def delete_task(request, id):
    asd = Task.objects.get(author=request.user, id=id)
    asd.delete()    
    return redirect('home')

