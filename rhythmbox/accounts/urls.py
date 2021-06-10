from django.urls import path
from .views import register_user, logout_user, login_user, account_details

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("account/details/", account_details, name="account_details"),
]
