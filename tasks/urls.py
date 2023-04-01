from django.urls import path
from .views import *

urlpatterns = [
    path('create_task/', create_task, name='create_task'),
    path('my_task/', my_task, name='my_task'),
    path('view_task/<int:id>/', view_task, name='view_task'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
]
