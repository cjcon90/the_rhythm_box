from django.urls import path
from .views import (
    register_user,
    logout_user,
    login_user,
    account_details,
    edit_account_details,
    add_address,
    edit_address
)

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("account/details/", account_details, name="account_details"),
    path(
        "account/details/edit/",
        edit_account_details,
        name="edit_account_details",
    ),
    path("account/address/new/", add_address, name="add_address"),
    path("account/address/edit/", edit_address, name="edit_address"),
]
