from .models import *
from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User

class passwordchangingform(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password','id':"password1","autocomplete":"current-password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete":"new-password",'class': 'form-control','type':'password','id':"password2","style":"position:relative;"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password','id':"password3"}))
    class meta:
        model = User
        fields = ('old_password','new_password1','new_password2')

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'EMail ID',
        'type': 'email',
        'name': 'email'
        }))

class PasswordResetConfirmViewForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetConfirmViewForm, self).__init__(*args, **kwargs)
    new_password1 = forms.CharField(label='', widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Password',
    'type': 'password',
    'name': 'new_password1'
    }))
    new_password2 = forms.CharField(label='', widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Confirm Password',
    'type': 'password',
    'name': 'new_password1'
    }))