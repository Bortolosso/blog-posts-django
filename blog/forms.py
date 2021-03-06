from .models import Comment, UserProfileInfo, Post

from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'body',
        )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = (
            'username',
            'password',
            'email'
        )


class UserPostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = (
            'tittle',
            'slug',
            'content',
            'status'
        )
