from django import forms
from .models import Profile

class PostForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["product_img"]