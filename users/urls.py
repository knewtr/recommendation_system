from django.urls import path

from users.apps import UsersConfig
from users.views import (
    LoginView,
    LogoutView,
    ProfileView,
    RegisterView,
    UserListView,
    UserUpdateView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="books:home"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("update/", UserUpdateView.as_view(), name="profile_update"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("list/", UserListView.as_view(), name="user_list"),
]
