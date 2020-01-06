from .models import Comment, UserProfileInfo

from django import forms
from django.contrib.auth.models import User

from .models import UserProfileInfo

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'name', 
            'email', 
            'body'
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

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = (
            'name_dica',
        )
    