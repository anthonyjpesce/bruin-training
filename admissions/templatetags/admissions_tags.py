from django import template

# Open up the templatetag registry
register = template.Library()


def multiply(value, arg):
    """
    Multiply the arg by the value
    """
    return value * int(arg)

register.filter_function(multiply)
