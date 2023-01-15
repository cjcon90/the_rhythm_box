import re
from django import template

register = template.Library()


@register.filter
def splitlines(value):
    return value.splitlines()


@register.filter
def bullets(value):
    return [f'• {re.sub(r"^- ", "", s)}' for s in splitlines(value)]
