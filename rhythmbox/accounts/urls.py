from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register_user,
    logout_user,
    login_user,
    account_details,
    edit_account_details,
    add_address,
    edit_address,
    my_orders,
    newsletter_subscribe,
    contact,
    contact_success
)

urlpatterns = [
    path("newsletter_subscribe/", newsletter_subscribe, name="newsletter_subscribe"),
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
    path("account/orders/", my_orders, name="my_orders"),
    path(
        "account/password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "account/password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "account/password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "account/password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("contact/", contact, name="contact"),
    path("contact_success/", contact_success, name="contact_success"),
]
