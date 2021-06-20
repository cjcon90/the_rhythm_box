from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "first_name",
            "last_name",
            "street_address_1",
            "street_address_2",
            "town_or_city",
            "county",
            "postcode",
            "country",
            "phone_number",
        )
        labels = {
            "street_address_1": "Address Line 1",
            "street_address_2": "Address Line 2 (optional)",
        }
