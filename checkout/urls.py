from django.urls import path
from .views import (
    checkout,
    checkout_success,
    cache_checkout
)
from .webhooks import webhook

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("checkout_success/<order_number>/", checkout_success, name="checkout_success"),
    path("checkout/cache_checkout_data/", cache_checkout, name="cache_checkout"),
    path("wh/", webhook, name="webhook")
]
