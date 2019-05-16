import re

from enum import Enum

BASE_URL = 'https://f1.bilder-fee.de'
TOKEN = 'T'
RE_COLOR = re.compile('([0-9a-f]{3})|([0-9-a-f]{6})')


def by_pass(x):
    return x if x else None


def to_nr_range(x, mn=0, mx=365):
    return max(mn, min(mx, x)) if isinstance(x, (int, float)) else None


def bool_2_int(x):
    return 1 if x else None


def trans_enum(x):
    return x.value if isinstance(x, Enum) else None


def trans_color(x):
    return x if x and RE_COLOR.search(x) else None


ALLOWED_OPTIONS = {
    "width": lambda x: to_nr_range(x, mn=1, mx=90000),
    "height": lambda x: to_nr_range(x, mn=1, mx=90000),
    "flip": lambda x: bool_2_int(x),
    "flop": lambda x: bool_2_int(x),
    "crop": lambda x: bool_2_int(x),
    "rotate": lambda x: to_nr_range(x, mn=-360, mx=360),
    "sharpen": lambda x: to_nr_range(x, mn=1, mx=100),
    "blur": lambda x: to_nr_range(x, mn=1, mx=100),
    "negate": lambda x: bool_2_int(x),
    "dpr": lambda x: to_nr_range(x, mn=0.5, mx=5),
    "fit": lambda x: bool_2_int(x),
    "quality": lambda x: to_nr_range(x, mn=50, mx=100),
    "gravity": lambda x: trans_enum(x),
    "progressive": lambda x: bool_2_int(x),
    "format": lambda x: trans_enum(x),
    "background": lambda x: trans_color(x),
    "enlarge": lambda x: bool_2_int(x),
    "extend": lambda x: bool_2_int(x),
    "greyscale": lambda x: bool_2_int(x),
    "grayscale": lambda x: bool_2_int(x),
    "embed": lambda x: bool_2_int(x),
    "w": lambda x: lambda x: to_nr_range(x, mn=1, mx=90000),
    "h": lambda x: lambda x: to_nr_range(x, mn=1, mx=90000),
    "rot": lambda x: to_nr_range(x, mn=-360, mx=360),
    "bl": lambda x: to_nr_range(x, mn=1, mx=100),
    "sh": lambda x: bool_2_int(x),
    "q": lambda x: to_nr_range(x, mn=50, mx=100),
    "g": lambda x: trans_enum(x),
    "ext": lambda x: trans_enum(x),
    "fmt": lambda x: trans_enum(x),
    "bg": lambda x: trans_color(x),
    "gray": lambda x: bool_2_int(x),
    "xt": lambda x: bool_2_int(x),
}


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


class Ext(Enum):
    JPEG = 'jpg'
    PNG = 'png'
    GIF = 'gif'
    WEBP = 'webp'
    ICO = 'ico'


MAP_VALUES = {
    True: 1,
    False: 0
}


def map_values(v):
    if isinstance(v, Enum):
        return v.value
    else:
        return MAP_VALUES.get(v, v)


def url(url, **kwargs):
    options = ','.join(
        '{}:{}'.format(k, ALLOWED_OPTIONS[k](v))
        for k, v in kwargs.items()
        if k in ALLOWED_OPTIONS and ALLOWED_OPTIONS[k](v) is not None
    )

    return '{base_url}/{token}/{options}/{url}'.format(
        base_url=kwargs.get('base_url', BASE_URL),
        token=kwargs.get('token', TOKEN),
        options=options,
        url=url[1:] if url[0] == '/' else url
    )
