from django.template import Library
import hashlib

register = Library()

@register.filter
def gravatar(value):
    return hashlib.md5(value).hexdigest()
