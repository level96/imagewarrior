import re

from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

from imagewarrior.imagewarrior import url

register = template.Library()

SRC_ATTRS = {'gravity', 'gravity_focus', 'resize_type', 'quality', 'blur', 'sharpen', 'ext', 'dpr', 'background'}
REG_SCHEME = re.compile('^http(s)?://')


@register.simple_tag
def image_src(img, dim, **kwargs):
    width, height = dim.split('x')

    data = {
        'width': int(width),
        'height': int(height),
        'token': settings.BILDERFEE_TOKEN
    }
    full_url = '{}{}'.format(REG_SCHEME.sub('', settings.BASE_URL), img)
    data.update(**kwargs)

    return url(full_url, **data)


@register.simple_tag
def image(img, dim, lazy=True, **kwargs):
    src_kwargs = {}
    img_attrs = {}
    for k, v in kwargs.items():
        if k in SRC_ATTRS:
            src_kwargs[k] = v
        else:
            img_attrs[k] = v

    img_src = image_src(img, dim, **src_kwargs)
    src = 'src'
    if lazy:
        src = 'data-src'
        cls = '{}{}'.format(img_attrs.get('class', ''), ' iw-lazy')
        img_attrs['class'] = cls

    img_attrs[src] = img_src

    html = '<img {}/>'.format(' '.join('{}="{}"'.format(k, v) for k, v in img_attrs.items()))
    return mark_safe(html)
