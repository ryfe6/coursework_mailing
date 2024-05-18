from django.shortcuts import render
from users.models import User
from django.views.generic import CreateView, UpdateView, TemplateView, FormView, View
# Create your views here.
from users.forms import UserRegisterForm, UserProfileForm, UserAuthenticationForm, UserPasswordResetForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('mailing:mailing_list')


class ProfileView(LoginRequiredMixin, UpdateView):
    """Profile view."""
    model = User
    form_class = UserProfileForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserLoginView(LoginView):
    """Авторизация пользователя."""
    model = User
    form_class = UserAuthenticationForm
    template_name = 'users/login.html'


class UserLogoutView(BaseLogoutView):
    """Выход пользователя из своей учетной записи."""
    pass
