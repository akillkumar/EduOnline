from django import template

register = template.Library()

@register.filter
def split_and_join(value, delimiter):
    return ' '.join(value.split(delimiter))

template.Library.filter(split_and_join)