import random

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, ListView, TemplateView,
                                  UpdateView, View)

# Create your views here.
from users.forms import (UserAuthenticationForm, UserManagerForm,
                         UserProfileForm, UserRegisterForm)
from users.models import User


class UserManagerListView(ListView):
    model = User
    form_class = UserManagerForm
    template_name = "users/usermanager_list.html"
    login_url = reverse_lazy("users:login")


class UserManagerUpdateView(UpdateView):
    model = User
    fields = [
        "is_active",
    ]
    template_name = "users/usermanager_form.html"
    success_url = reverse_lazy("users:user_list")
    login_url = reverse_lazy("users:login")


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:verification")

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save()
            send_mail(
                subject="Подтверждение",
                message=f"Код верификации: {new_user.ver_code}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email],
            )
        return super().form_valid(form)


class VerificationTemplateView(TemplateView):
    template_name = "users/verificated_email.html"

    def post(self, request):
        ver_cod = request.POST.get("confirm_code")
        user_code = User.objects.filter(ver_code=ver_cod).first()

        if user_code is not None and user_code.ver_code == ver_cod:
            user_code.is_active = True
            user_code.save()
            return redirect("users:login")
        else:
            return redirect("users:register")


class ProfileView(LoginRequiredMixin, UpdateView):
    """Profile view."""

    model = User
    form_class = UserProfileForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:profile")
    login_url = reverse_lazy("users:login")

    def get_object(self, queryset=None):
        return self.request.user


class UserLoginView(LoginView):
    """Авторизация пользователя."""

    model = User
    form_class = UserAuthenticationForm
    template_name = "users/login.html"


class UserLogoutView(BaseLogoutView):
    """Выход пользователя из своей учетной записи."""

    pass
