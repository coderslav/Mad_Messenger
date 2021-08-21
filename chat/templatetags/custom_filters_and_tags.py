from django import template

register = template.Library()


@register.filter(name='modulo')
def modulo(value):
    return value % 2


@register.filter(name='to_string')
def to_string(value):
    return str(value)
