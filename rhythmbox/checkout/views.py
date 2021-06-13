from products.models import Product
from .models import OrderLineItem, Order
from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from .forms import OrderForm
from django.conf import settings
from cart.contexts import cart_contents
from django.contrib import messages
from django.utils.safestring import mark_safe
import stripe


def checkout(request):
    context = {}
    # Submit form if valid
    if request.POST:
        cart = request.session.get("cart", {})
        form = OrderForm(request.POST)
        if form.is_valid():
            order_number = form.save()
            order = Order.objects.get(order_number=order_number)
            for item_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products in your bag wasn't found in our database.\n\
                                Please call us for assistance!"
                        ),
                    )
                    order.delete()
                    return redirect("cart")
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            context["order_form"] = form
    else:  # GET request
        form = OrderForm()
        context["order_form"] = form
        # Load Cart
        cart = request.session.get("cart", {})
        if not cart:
            return redirect("cart")
        current_cart = cart_contents(request)
        total = current_cart["grand_total"]
        # Create Stripe Payment Intent
        stripe_total = round(total * 100)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if not settings.STRIPE_PUBLIC_KEY:
            messages.error(
                request,
                "Stripe public key is missing.\n\
                    Did you forget to set it in your environ?",
            )

    context["order_form"] = OrderForm()
    context["stripe_public_key"] = settings.STRIPE_PUBLIC_KEY
    context["client_secret"] = intent.client_secret
    return render(request, "checkout/checkout.html", context)


def checkout_success(request, order_number):
    context = {}
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request,
        mark_safe(f"Order successfully processed!</br>\
            Your order number is <strong>{order_number}</strong>.</br>\
                A confirmation email will be sent to <strong>{order.email}</strong>."),
    )
    context["order"] = order
    return render(request, "checkout/checkout_success.html", context)
