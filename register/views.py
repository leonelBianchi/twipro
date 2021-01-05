from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, EditProfileForm, ProfilePageForm
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm 
from django.views.generic import DetailView, CreateView
from main.models import Profile


# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})

def update(response):
    form = UserChangeForm

    return render(response, "register/editprofile.html", {"form": form})

class EditProfile(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "register/editprofile.html"
    success_url = reverse_lazy("home")   

    def get_object(self):
        return self.request.user
      

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("password_success")   

def password_success(request):
    return render(request, "register/password_success.html")

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = "register/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        
        context["page_user"] = page_user

        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "register/edit_profile_page.html"
    fields = ["bio", "profile_pic", "website_url", "twitter_url",
    "github_url", "twitch_url"]

    success_url = reverse_lazy("home")

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "register/create_user_profile_page.html"
    #fields = "__all__"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
