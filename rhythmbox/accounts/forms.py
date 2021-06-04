from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    newsletter = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=(
            (True, "Yes, subscribe me to the list"),
            (False, "No thank you"),
        ),
        widget=forms.RadioSelect,
        initial=False,
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
