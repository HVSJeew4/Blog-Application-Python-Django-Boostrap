from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .form import UserLoginForm, PwdResetForm, PwdChangeForm, PwdResetForm, PwdResetConfirmForm

app_name = 'acoounts'

urlpatterns = [
     path('login/', auth_views.LoginView.as_view(template_name="registration/login.html",
                                                authentication_form=UserLoginForm), name='login'),
]
