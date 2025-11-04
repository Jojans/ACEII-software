from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except:
        return value

@register.filter
def split(value, separator):
    """Divide un string usando el separador dado. Si el valor es None, retorna una lista vacía."""
    if value is None:
        return []
    return value.split(separator)

@register.filter
def zip_lists(list1, list2):
    """
    Combina dos listas (producto, cantidad, precio) en tuplas.
    """
    return zip(list1, list2)
