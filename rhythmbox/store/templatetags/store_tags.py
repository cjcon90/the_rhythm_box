from django import template

register = template.Library()

# Source: https://stackoverflow.com/a/16609591
@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()