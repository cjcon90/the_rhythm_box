from django import template
from products.models import Product

register = template.Library()

@register.simple_tag
def cart_in_stock(cart):
    in_stock = True
    for item in cart:
        if Product.objects.get(pk=item['item_id']).stock == 0:
            in_stock = False
            break
    return in_stock
