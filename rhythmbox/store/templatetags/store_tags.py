from django import template

register = template.Library()

# Source: https://stackoverflow.com/a/16609591
@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()


@register.simple_tag
def display_count(count_type, count):
    """
    Tag for displaying items such as
    ratings or reviews on web page
    """
    if count == 0:
        return f"No {count_type}s yet"
    elif count == 1:
        return f"1 {count_type.title()}"
    else:
        return f"{count} {count_type.title()}s"


@register.simple_tag
def display_stock(count):
    """
    Tag for displaying items such as
    ratings or reviews on web page
    """
    if count > 50:
        return f"50+"
    elif count > 25:
        return f"25+"
    elif count > 10:
        return f"10+"
    else:
        return f"{count}"
