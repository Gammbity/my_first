from django import template

register = template.Library()

@register.filter
def to_upper(value, number):
    s = ''
    for i, v in enumerate(value, 1):
        if value.isalpha() and i <= int(number):
            s += v.upper()
        else:
        s += v    
    return s