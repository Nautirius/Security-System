from django import template

register = template.Library()

@register.filter
def camera_count(zones):
    return sum(zone.cameras.count() for zone in zones)