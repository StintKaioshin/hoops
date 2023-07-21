from django import template
register = template.Library()

@register.filter
def split(value, key):
    """
        Returns the value turned into a list where each item is an
        item in the original string separated by the key.
    """
    return value.split(key)
