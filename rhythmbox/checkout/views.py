from django.shortcuts import render, redirect
from .forms import OrderForm
from django.conf import settings
from cart.contexts import cart_contents
import stripe


def checkout(request):
    context = {}

    cart = request.session.get("cart", {})
    if not cart:
        return redirect("cart")
    current_cart = cart_contents(request)
    total = current_cart["grand_total"]
    stripe_total = round(total * 100)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    context["order_form"] = OrderForm()

    if not settings.STRIPE_PUBLIC_KEY:
        messages.error(
            request,
            "Stripe public key is missing. Did you forget to set it in your environ?",
        )

    context["stripe_public_key"] = settings.STRIPE_PUBLIC_KEY
    context["client_secret"] = intent.client_secret
    return render(request, "checkout/checkout.html", context)
