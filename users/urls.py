from django.urls import path

from users.apps import UsersConfig
from users.views import (ProfileView, RegisterView, UserLoginView,
                         UserLogoutView, UserManagerListView,
                         UserManagerUpdateView, VerificationTemplateView)

app_name = UsersConfig.name

urlpatterns = [
    path("", UserLoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("verificated/", VerificationTemplateView.as_view(), name="verification"),
    path("user/list", UserManagerListView.as_view(), name="user_list"),
    path("user/ban/<int:pk>", UserManagerUpdateView.as_view(), name="user_ban"),
]
