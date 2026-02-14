from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Form for creating/editing posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# Optional: custom user registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
