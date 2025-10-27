from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Usage in template: {{ mydict|get_item:key }}
    Returns value of dictionary[key] or '-' if not found.
    """
    if not dictionary:
        return "-"
    return dictionary.get(key, "-")
