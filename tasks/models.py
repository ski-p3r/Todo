from django.db import models
from accounts.models import Account, Profile

# Create your models here.

class Task(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    author  = models.ForeignKey(Account, on_delete=models.CASCADE)
    task    = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    date    = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task
    