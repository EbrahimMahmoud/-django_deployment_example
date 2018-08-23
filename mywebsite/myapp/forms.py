from django import forms
from django.core import validators
from django.forms import ModelForm
from django.contrib.auth.models import User
from myapp.models import UserProfileInfo


class UserForm(forms.ModelForm):
    """ put validtors here if you want/this is bulit in User"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    ''' this is from models.py'''
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
