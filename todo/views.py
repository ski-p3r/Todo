from django.shortcuts import render
from tasks.models import Task
from accounts.models import Account, Profile

def home(request):
    task = Task.objects.all()
    context = {
        'task': task,
    }
    return render(request, 'index.html', context)