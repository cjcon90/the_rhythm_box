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
    if count == 0:
        return f"No {count_type}s yet"
    elif count == 1:
        return f"1 {count_type.title()}"
    else:
        return f"{count} {count_type.title()}s"
