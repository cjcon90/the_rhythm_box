import os, json

import stripe

from django.contrib import messages
from django.utils.safestring import mark_safe
from django.http import QueryDict
from django.forms.models import model_to_dict
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
)

from cart.contexts import cart_contents
from products.models import Product
from accounts.models import Account, Address
from .models import OrderLineItem, Order
from .forms import OrderForm



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


@login_required
def checkout(request):
    context = {}
    # Submit form if valid
    if request.POST:
        cart = request.session.get("cart", {})
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
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
            for item in OrderLineItem.objects.filter(order=order):
                # if complete order is successful, reduce stock of each item purchased by quantity
                item.product.stock -= item.quantity
                item.product.save()

            # Empty Cart
            del request.session["cart"]

            # Add default shipping address, if ticked
            if request.POST.get("make_default_shipping"):
                address_info = model_to_dict(order)
                # Update existing address or create new one
                address_obj, created = Address.objects.update_or_create(
                    user=request.user,
                    defaults={
                        "street_address_1": order.street_address_1,
                        "street_address_2": order.street_address_2,
                        "town_or_city": order.town_or_city,
                        "county": order.county,
                        "postcode": order.postcode,
                        "phone_number": order.phone_number,
                    },
                )

            # Email Order Confirmation
            msg_content = {
                "order": order,
                "items": [item for item in order.lineitems.all()],
                "contact_email": os.environ["EMAIL_USER"],
            }
            msg_plain = render_to_string(
                "checkout/order_confirmation_email.txt",
                msg_content,
            )
            msg_html = render_to_string(
                "checkout/order_confirmation_email.html",
                msg_content,
            )
            subject = f"RhythmBox Order Confirmation: #{order.order_number}"
            from_email = os.environ["EMAIL_USER"]
            try:
                send_mail(
                    subject,
                    msg_plain,
                    from_email,
                    [order.user.email],
                    fail_silently=True,
                    html_message=msg_html,
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            context["order_form"] = form
    else:  # GET request
        # Add user name to form by default
        details = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }
        try:
            # add user address (if exists)
            details.update(model_to_dict(request.user.address))
        except Address.DoesNotExist:
            pass
        finally:
            form = OrderForm(initial=details)
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
