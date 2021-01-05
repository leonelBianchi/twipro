"""players URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('main.urls')), # main will be the name of your app
    path("register/", v.register, name="register"),
    path('admin/', admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path("update/", v.update, name="update"),
    path("editprofile/", v.EditProfile.as_view(), name="editprofile"),
    path("password/", v.PasswordsChangeView.as_view(template_name="register/change-password.html")),
    path("password_success/", v.password_success, name="password_success"),
    path("<int:pk>/profile/", v.ShowProfilePageView.as_view(), name="show_profile_page"),
    path("<int:pk>/edit_profile_page/", v.EditProfilePageView.as_view(), name="edit_profile_page"),
    path("create_profile_page/", v.CreateProfilePageView.as_view(), name="create_profile_page"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

