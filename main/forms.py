from django import forms
from django.contrib.auth.models import User
from .models import CustomUser,TextTask


class UserRegisterForm(forms.ModelForm):

    last_name = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['phone_number']
        # fields = ['last_name', 'first_name',
        #           'email', 'phone_number', 'username', 'password']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name',
                  'email', 'username']


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number']



class TextTaskForm(forms.ModelForm):
    class Meta:
        model=TextTask
        fields = ['source_text','source_file']

