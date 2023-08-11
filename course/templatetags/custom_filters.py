from django import template

register = template.Library()

@register.filter(name='custom_range')
def custom_range(start, end):
    return range(start, end + 1)
