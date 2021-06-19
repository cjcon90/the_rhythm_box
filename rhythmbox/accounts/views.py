from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import (
    RegistrationForm,
    AccountAuthenticationForm,
    EditAccountForm,
    AddressForm,
)
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.forms.models import model_to_dict
from .models import Address
from checkout.models import Order


@login_required
def account_details(request):
    context = {}
    user = request.user
    return render(request, "accounts/account_details.html", context)


@login_required
def edit_account_details(request):
    context = {}
    user = request.user
    if request.POST:
        form = EditAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account details updated")
            return redirect("account_details")
        else:
            context["edit_account_form"] = form

    else:
        form = EditAccountForm(initial=model_to_dict(user))
        context["edit_account_form"] = form
    return render(request, "accounts/edit_account_details.html", context)


@login_required
def add_address(request):
    context = {}
    user = request.user
    if request.POST:
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, f"Address saved")
            return redirect("account_details")
        else:
            context["address_form"] = form
    else:
        form = AddressForm()
        context["address_form"] = form
        context["type"] = "Add"
    return render(request, "accounts/address.html", context)

@login_required
def edit_address(request):
    context = {}
    address = request.user.address
    if request.POST:
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, f"Address updated")
            return redirect("account_details")
        else:
            context["address_form"] = form
    else:
        form = AddressForm(initial=model_to_dict(address))
        context["address_form"] = form
        context["type"] = "Edit"
    return render(request, "accounts/address.html", context)

@login_required
def my_orders(request):
    context = {}
    context["orders"] = Order.objects.filter(user=request.user)
    return render(request, "accounts/my_orders.html", context)



def register_user(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            messages.success(
                request,
                f"Thanks for registering, {request.user.first_name}! You are now logged in 🙂",
            )
            return redirect("home")
        else:
            context["registration_form"] = form
    else:  # GET request
        form = RegistrationForm()
        context["registration_form"] = form
    return render(request, "accounts/register.html", context)


def logout_user(request):
    logout(request)
    return redirect("/")


def login_user(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f"Welcome back, {request.user.first_name}! 🙂"
                )
                return redirect("home")
        else:
            messages.error(request, f"Incorrect login details")
            return redirect("login")

    else:
        form = AccountAuthenticationForm()

    context["login_form"] = form
    return render(request, "accounts/login.html", context)
