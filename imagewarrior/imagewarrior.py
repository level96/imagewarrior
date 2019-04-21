from enum import Enum

base_url = 'https://leo.imagewarrior.de'


class Gravity(Enum):
    SMART = 'sm'
    NORTH = 'no'
    SOUTH = 'so'
    EAST = 'ea'
    WEST = 'we'
    CENTER = 'ce'
    NORTH_EAST = 'noea'
    NORTH_WEST = 'nowe'
    SOUTH_EAST = 'soea'
    SOUTH_WEST = 'sowe'
    FOCUS = 'fp'


class Resize(Enum):
    FIT = 'fit'
    FILL = 'fill'
    CROP = 'crop'


class Ext(Enum):
    JPEG = 'jpg'
    PNG = 'png'
    GIF = 'gif'
    WEBP = 'webp'
    ICO = 'ico'


def url(url, width, height, resize=True, resize_type=Resize.FIT, enlarge=0, dpr=1, gravity=None, gravity_focus=None,
        quality=None, background=None, blur=None, sharpen=None, ext=None):
    g = ''
    if gravity:
        grav_val = gravity.value
        if gravity == Gravity.FOCUS:
            grav_val = 'fp:{}:{}'.format(*gravity_focus)
        g = '/g:{}'.format(grav_val)

    s = '/s:{}:{}'.format(width, height)
    rs = '/rs:{}:{}:{}:{}'.format(resize_type.value, width, height, enlarge)

    return '{base_url}/insecure{rs}{g}{dpr}{q}{bg}{bl}{sh}/plain/{url}{ext}'.format(
        base_url=base_url,
        url=url[1:] if url[0] == '/' else url,
        g=g,
        rs=rs if resize else s,
        bl='/bl:{}'.format(blur) if blur and blur > 0 else '',
        sh='/sh:{}'.format(sharpen) if sharpen and sharpen > 0 else '',
        bg='/bg:{}:{}:{}'.format(*background) if background else '',
        q='/q:{}'.format(quality) if quality and 1 <= quality <= 100 else '',
        dpr='/dpr:{}'.format(dpr) if dpr and dpr > 1 else '',
        ext='@{}'.format(ext.value) if ext else '',
    )
