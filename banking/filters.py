from django import template
import locale
locale.setlocale(locale.LC_ALL, '')
register = template.Library()


@register.filter(name='currency')
def currency(value):
    return locale.currency(value, grouping=True)