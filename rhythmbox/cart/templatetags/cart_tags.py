from django import template
from products.models import Product

register = template.Library()


@register.simple_tag
def cart_in_stock(cart):
    """
    tag to check before user goes from cart to
    checkout that all cart items are still in stock
    """
    in_stock = True
    for item in cart:
        if item["quantity"] > Product.objects.get(pk=item["item_id"]).stock:
            in_stock = False
            break
    return in_stock
