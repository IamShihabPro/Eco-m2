from django import template

register = template.Library()

def my_filter(value, arg):
    return value + " Middle Text " + arg

register.filter('custom_filter', my_filter)