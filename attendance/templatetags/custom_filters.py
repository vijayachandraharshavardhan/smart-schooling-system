from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Safely fetch a key from a dictionary in templates."""
    if not dictionary:
        return None
    return dictionary.get(key)
