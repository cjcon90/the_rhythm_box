from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.forms.models import model_to_dict
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from checkout.models import Order
from .models import Account, Address, NewsletterSub
from .forms import (
    RegistrationForm,
    AccountAuthenticationForm,
    EditAccountForm,
    DeleteAccountForm,
    AddressForm,
    ContactForm,
)


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
def delete_account(request):
    context = {}
    if request.POST:
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            email = request.user.email
            password = request.POST["password"]
            user = authenticate(email=email, password=password)
            if user:
                user.delete()
                messages.success(
                    request,
                    f"Your account has been deleted. Sorry to see you go! 👋",
                )
                return redirect("home")
            else:
                form.add_error("password", "Incorrect Password")
                context["delete_account_form"] = form
        else:
            context["delete_account_form"] = form
    else:
        form = DeleteAccountForm()
        context["delete_account_form"] = form
    return render(request, "accounts/delete_account.html", context)


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
            context["address_form"] = form
    else:
        form = AddressForm(initial=model_to_dict(address))
        context["address_form"] = form
        context["type"] = "Edit"
    return render(request, "accounts/address.html", context)


@login_required
def my_orders(request):
    context = {}
    context["orders"] = Order.objects.filter(user=request.user).order_by(
        "-date"
    )
    return render(request, "accounts/my_orders.html", context)


def register_user(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        redirect_url = request.POST.get("next") or "home"
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            if NewsletterSub.objects.filter(email=email).exists():
                NewsletterSub.objects.get(email=email).delete()
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            messages.success(
                request,
                f"Thanks for registering, {request.user.first_name}! You are now logged in 🙂",
            )
            return redirect(redirect_url)
        else:
            context["registration_form"] = form
    else:  # GET request
        form = RegistrationForm()
        context["registration_form"] = form
    return render(request, "accounts/register.html", context)


def logout_user(request):
    logout(request)
    messages.success(
        request, f"You have successfully logged out 👋"
    )
    return redirect("/")


def login_user(request):

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        redirect_url = request.POST.get("next") or "home"
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f"Welcome back, {request.user.first_name}! 🙂"
                )
                return redirect(redirect_url)
        else:
            messages.error(request, f"Incorrect login details")
            context["login_form"] = form

    else:
        form = AccountAuthenticationForm()
        if request.POST.get("next"):
            messages.error(
                request, f"You must be logged in to access this page"
            )
        context["login_form"] = form
    return render(request, "accounts/login.html", context)


def newsletter_subscribe(request):
    email = request.POST["email"]
    already_registered = Account.objects.filter(email=email).exists()
    already_subbed = NewsletterSub.objects.filter(email=email).exists()
    if already_subbed:
        pass
    elif already_registered:
        user = Account.objects.get(email=email)
        user.newsletter = True
        user.save()
    else:
        sub = NewsletterSub(email=email)
        sub.save()
    messages.success(request, "Thank you for subscribing to our newsletter!")
    return redirect(request.GET.get("next"))


def contact(request):
    context = {}

    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            from_name = form.cleaned_data["from_name"]
            mail_msg = f"Message from: {from_name}\n\n{message}\n\nReturn email address: {from_email}"
            try:
                send_mail(subject, mail_msg, from_email, ["cjcon90@pm.me"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(
                request,
                "Message successfully sent!\nThanks for getting in touch 🙂",
            )
            return redirect("contact_success")
        else:
            context["contact_form"] = form
    else:
        if request.user.is_authenticated:
            form = ContactForm(
                initial={
                    "from_email": request.user.email,
                    "from_name": request.user.first_name,
                }
            )
        else:
            form = ContactForm()
    context["contact_form"] = form
    return render(request, "accounts/contact.html", context)


def contact_success(request):
    return render(request, "accounts/contact_success.html")
