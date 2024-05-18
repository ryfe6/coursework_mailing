from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm
from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя."""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    """Профиль пользователя"""
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserAuthenticationForm(StyleFormMixin, AuthenticationForm):
    """Форма аутентификация пользователя."""
    pass


class UserPasswordResetForm(StyleFormMixin, PasswordResetForm):
    """Форма сброса пароля пользователем."""
    class Meta:
        model = User
        fields = ('email',)