import os

from django import template

from djangoProject import settings

register = template.Library()

@register.simple_tag(name='media_path')
def mediapath(image_path):
    media_url = settings.MEDIA_URL
    full_path = os.path.join(media_url, str(image_path))
    return full_path