import pytest

from imagewarrior.imagewarrior import Resize
from imagewarrior.imagewarrior import Gravity
from imagewarrior.imagewarrior import Ext
from imagewarrior.imagewarrior import url


@pytest.mark.parametrize('params, exp_url', [
    ({'width': 800, 'height': 400, 'resize': False}, 'insecure/s:800:400/plain/IMG-URL'),

    ({'width': 800, 'height': 400, 'resize_type': Resize.FILL}, 'insecure/rs:fill:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'resize_type': Resize.FIT}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'resize_type': Resize.CROP}, 'insecure/rs:crop:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'enlarge': 1}, 'insecure/rs:fit:800:400:1/plain/IMG-URL'),
    # Gravity
    ({'width': 800, 'height': 400, 'gravity': Gravity.CENTER}, 'insecure/rs:fit:800:400:0/g:ce/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.SMART}, 'insecure/rs:fit:800:400:0/g:sm/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.EAST}, 'insecure/rs:fit:800:400:0/g:ea/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.NORTH}, 'insecure/rs:fit:800:400:0/g:no/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.NORTH_EAST}, 'insecure/rs:fit:800:400:0/g:noea/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.NORTH_WEST}, 'insecure/rs:fit:800:400:0/g:nowe/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.SOUTH}, 'insecure/rs:fit:800:400:0/g:so/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.SOUTH_EAST}, 'insecure/rs:fit:800:400:0/g:soea/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.SOUTH_WEST}, 'insecure/rs:fit:800:400:0/g:sowe/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.WEST}, 'insecure/rs:fit:800:400:0/g:we/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.FOCUS, 'gravity_focus': (10, 11)}, 'insecure/rs:fit:800:400:0/g:fp:10:11/plain/IMG-URL'),
    # DPR
    ({'width': 800, 'height': 400, 'dpr': None}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'dpr': 0}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'dpr': 0.5}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'dpr': 1}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'dpr': 2}, 'insecure/rs:fit:800:400:0/dpr:2/plain/IMG-URL'),
    # Quality
    ({'width': 800, 'height': 400, 'quality': None}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': ''}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': -10}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': 101}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': 1}, 'insecure/rs:fit:800:400:0/q:1/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': 80}, 'insecure/rs:fit:800:400:0/q:80/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': 100}, 'insecure/rs:fit:800:400:0/q:100/plain/IMG-URL'),
    # Background
    ({'width': 800, 'height': 400, 'background': (10, 11, 12)}, 'insecure/rs:fit:800:400:0/bg:10:11:12/plain/IMG-URL'),
    # Blur
    ({'width': 800, 'height': 400, 'blur': -1}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'blur': 1}, 'insecure/rs:fit:800:400:0/bl:1/plain/IMG-URL'),
    # Sharpen
    ({'width': 800, 'height': 400, 'sharpen': -1}, 'insecure/rs:fit:800:400:0/plain/IMG-URL'),
    ({'width': 800, 'height': 400, 'sharpen': 2}, 'insecure/rs:fit:800:400:0/sh:2/plain/IMG-URL'),
    # File Extension
    ({'width': 800, 'height': 400, 'ext': Ext.GIF}, 'insecure/rs:fit:800:400:0/plain/IMG-URL@gif'),
    ({'width': 800, 'height': 400, 'ext': Ext.ICO}, 'insecure/rs:fit:800:400:0/plain/IMG-URL@ico'),
    ({'width': 800, 'height': 400, 'ext': Ext.JPEG}, 'insecure/rs:fit:800:400:0/plain/IMG-URL@jpg'),
    ({'width': 800, 'height': 400, 'ext': Ext.PNG}, 'insecure/rs:fit:800:400:0/plain/IMG-URL@png'),
    ({'width': 800, 'height': 400, 'ext': Ext.WEBP}, 'insecure/rs:fit:800:400:0/plain/IMG-URL@webp'),
])
def test_url(params, exp_url):
    res = url('IMG-URL', **params)

    exp_url_full = 'http://localhost:8080/{0}'.format(exp_url)
    assert res == exp_url_full

