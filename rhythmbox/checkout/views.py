from products.models import Product
from .models import OrderLineItem, Order
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
)
from django.views.decorators.http import require_POST
from .forms import OrderForm
from django.conf import settings
from cart.contexts import cart_contents
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.http import QueryDict
import stripe
import json


@require_POST
def cache_checkout(request):
    try:
        data = json.loads(request.body)
        # Payment intent ID = pid
        pid = data["client_secret"].split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "cart": json.dumps(request.session.get("cart", {})),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be processes right now. Please try again later",
        )
        return HttpResponse(content=e, status=400)


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
        form = OrderForm(
            {
                "first_name": "Ciaran",
                "last_name": "Concannon",
                "email": "cjcon90@pm.me",
                "phone_number": "0876723100",
                "town_or_city": "Dublin 6",
                "country": "IE",
                "street_address_1": "Apartment 41",
                "street_address_2": "Rathmines Town Center",
                "postcode": "D06 E221",
                "county": "Dublin",
            }
        )
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

    context["stripe_public_key"] = settings.STRIPE_PUBLIC_KEY
    context["client_secret"] = intent.client_secret
    return render(request, "checkout/checkout.html", context)


def checkout_success(request, order_number):
    context = {}
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request,
        mark_safe(f"Order Complete! 🙂"),
    )
    context["order"] = order
    return render(request, "checkout/checkout_success.html", context)
