from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ['date']
    list_display = ['author', 'task', 'description', 'date']

admin.site.register(Task, TaskAdmin)