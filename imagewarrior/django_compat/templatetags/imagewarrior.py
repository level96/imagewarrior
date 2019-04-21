import re

from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

from imagewarrior.imagewarrior import Resize
from imagewarrior.imagewarrior import url

register = template.Library()

SRC_ATTRS = {'gravity', 'gravity_focus', 'resize_type', 'quality', 'blur', 'sharpen', 'ext', 'dpr', 'background'}
REG_SCHEME = re.compile('^http(s)?://')


@register.simple_tag
def image_src(img, dim, gravity=None, gravity_focus=None, resize_type=Resize.FILL, quality=None, blur=None,
              sharpen=None, ext=None, dpr=None, background=None):
    width, height = dim.split('x')
    gfoc = gravity_focus.split(',') if gravity_focus else None
    bg = background.split(',') if background else None

    full_url = '{}{}'.format(REG_SCHEME.sub('', settings.BASE_URL), img)
    return url(full_url, width=width, height=height, gravity=gravity, gravity_focus=gfoc, resize_type=resize_type,
               quality=quality, blur=blur, sharpen=sharpen, ext=ext, dpr=dpr, background=bg)


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
