from django import template
from topics.models import *

register = template.Library()


@register.simple_tag()
def get_sections():
    return Section.objects.all()
