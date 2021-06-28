from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account, Address


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    newsletter = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=(
            (True, "Yes, subscribe me to the newsletter"),
            (False, "No thank you"),
        ),
        widget=forms.RadioSelect,
        initial=True,
    )

    class Meta:
        model = Account
        fields = (
            "email",
            "first_name",
            "last_name",
            "newsletter",
            "password1",
            "password2",
        )


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class EditAccountForm(forms.ModelForm):
    email = forms.EmailField(max_length=60)
    newsletter = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=(
            (True, "Yes, subscribe me to the newsletter"),
            (False, "No thank you"),
        ),
        widget=forms.RadioSelect,
        initial=True,
    )

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email", "newsletter")


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "street_address_1",
            "street_address_2",
            "town_or_city",
            "county",
            "postcode",
            "country",
            "phone_number",
        )
        labels = {
            "street_address_1": "Address 1",
            "street_address_2": "Address 2 (optional)",
            "town_or_city": "Town / City",
        }


class ContactForm(forms.Form):
    from_name = forms.CharField(
        required=True,
        label="Name",
        widget=forms.EmailInput(attrs={"placeholder": "What's your name?"}),
    )
    from_email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email address"}
        ),
    )
    subject = forms.CharField(
        max_length=60,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Email subject / title"}),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"placeholder": "What can we help you with?"}
        ),
    )
