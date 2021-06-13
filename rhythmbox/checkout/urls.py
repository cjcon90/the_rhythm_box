from django.urls import path
from .views import (
    checkout,
    checkout_success
)
from .webhooks import webhook

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("checkout_success/<order_number>/", checkout_success, name="checkout_success"),
    path("wh/", webhook, name="webhook")
]
