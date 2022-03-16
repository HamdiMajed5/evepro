from django import template

register = template.Library()


@register.simple_tag
def vuejs(var):
    return "{{ %s }}" % var
