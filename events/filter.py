from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def to_class_name(value):
    return value.__class__.__name__

