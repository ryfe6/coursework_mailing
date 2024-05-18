from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, UserLoginView, UserLogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    ]