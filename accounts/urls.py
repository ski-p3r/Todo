from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit_acc/', edit_acc, name='edit_acc'),
    path('acc_set/', acc_set, name='acc_set'),
    path('profile_pic/', profile_pic, name='profile_pic'),
    path('acc_del/', acc_del, name='acc_del'),
    path('change_password/', change_password, name='change_password'),
]
