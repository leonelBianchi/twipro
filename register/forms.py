from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from main.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_pic", "website_url", "twitter_url", "github_url", "twitch_url")
    
        wisgets = {
                "bio": forms.Textarea(attrs={"class": "form-control"}),
                #"profile_pic": forms.TextInput(attrs={"class": "form-control", "value": "", "id":"elder", "type":"hidden"}),
                "website_url": forms.TextInput(attrs={"class": "form-control"}),
                "twitter_url": forms.TextInput(attrs={"class": "form-control"}),
                "github_url": forms.TextInput(attrs={"class": "form-control"}),
                "twitch_url": forms.TextInput(attrs={"class": "form-control"}),

        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditProfileForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    is_active = forms.CharField(widget=forms.CheckboxInput(attrs={"class": "form-control"}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", 
        "last_login", "is_superuser", "is_staff", "is_active", "date_joined"]



   
        
