from django import template
from django.db.models import Max

register = template.Library()

@register.simple_tag
def get_primary_item(order):
    """
    Find the most expensive item in an order for
    displaying in user account order history
    """
    highest_price = order.lineitems.all().aggregate(Max("lineitem_total")).get(
        "lineitem_total_max"
    )
    return order.lineitems.filter(lineitem_total=highest_price)

@register.simple_tag
def get_primary_item_image(order):
    """
    Find the most expensive item in an order for
    displaying in user account order history
    """
    highest_price = order.lineitems.aggregate(Max("lineitem_total")).get(
        "lineitem_total__max"
    )
    lineitem = order.lineitems.get(lineitem_total=highest_price)
    image = lineitem.product.image.url
    return image
    