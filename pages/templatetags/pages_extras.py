from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.order_by('order')  #Obtener los objetos en orden de acuerdo al parametro de ordenación que elijamos
    return pages
