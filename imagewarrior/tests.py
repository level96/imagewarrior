import pytest

from imagewarrior.imagewarrior import Gravity
from imagewarrior.imagewarrior import Ext
from imagewarrior.imagewarrior import url


@pytest.mark.parametrize('params, exp_url', [
    ({'width': 800, 'height': 400}, 'T/width:800,height:400/IMG-URL'),
    ({'width': 800, 'height': 400, 'fit': True}, 'T/width:800,height:400,fit:1/IMG-URL'),
    ({'width': 800, 'height': 400, 'crop': True}, 'T/width:800,height:400,crop:1/IMG-URL'),
    ({'width': 800, 'height': 400}, 'T/width:800,height:400/IMG-URL'),
    ({'width': 800, 'height': 400, 'enlarge': 1}, 'T/width:800,height:400,enlarge:1/IMG-URL'),
    # Gravity
    ({'width': 800, 'height': 400, 'gravity': Gravity.CENTER}, 'T/width:800,height:400,gravity:ce/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.SMART}, 'T/width:800,height:400,gravity:sm/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.EAST}, 'T/width:800,height:400,gravity:ea/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.NORTH}, 'T/width:800,height:400,gravity:no/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.NORTH_EAST}, 'T/width:800,height:400,gravity:noea/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.NORTH_WEST}, 'T/width:800,height:400,gravity:nowe/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.SOUTH}, 'T/width:800,height:400,gravity:so/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.SOUTH_EAST}, 'T/width:800,height:400,gravity:soea/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.SOUTH_WEST}, 'T/width:800,height:400,gravity:sowe/IMG-URL'),
    ({'width': 800, 'height': 400, 'gravity': Gravity.WEST}, 'T/width:800,height:400,gravity:we/IMG-URL'),
    # DPR
    ({'width': 800, 'height': 400, 'dpr': None}, 'T/width:800,height:400/IMG-URL'),
    ({'width': 800, 'height': 400, 'dpr': 0}, 'T/width:800,height:400,dpr:0.5/IMG-URL'),
    ({'width': 800, 'height': 400, 'dpr': 0.5}, 'T/width:800,height:400,dpr:0.5/IMG-URL'),
    ({'width': 800, 'height': 400, 'dpr': 1}, 'T/width:800,height:400,dpr:1/IMG-URL'),
    ({'width': 800, 'height': 400, 'dpr': 2}, 'T/width:800,height:400,dpr:2/IMG-URL'),
    # Quality
    ({'width': 800, 'height': 400, 'quality': None}, 'T/width:800,height:400/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': ''}, 'T/width:800,height:400/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': -10}, 'T/width:800,height:400,quality:50/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': 101}, 'T/width:800,height:400,quality:100/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': 1}, 'T/width:800,height:400,quality:50/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': 80}, 'T/width:800,height:400,quality:80/IMG-URL'),
    ({'width': 800, 'height': 400, 'quality': 100}, 'T/width:800,height:400,quality:100/IMG-URL'),
    # Background
    ({'width': 800, 'height': 400, 'background': 'abc'}, 'T/width:800,height:400,background:abc/IMG-URL'),
    ({'width': 800, 'height': 400, 'background': 'aabbcc'}, 'T/width:800,height:400,background:aabbcc/IMG-URL'),
    ({'width': 800, 'height': 400, 'background': 'xyx'}, 'T/width:800,height:400/IMG-URL'),
    ({'width': 800, 'height': 400, 'background': 'abx'}, 'T/width:800,height:400/IMG-URL'),
    # Blur
    ({'width': 800, 'height': 400, 'blur': -1}, 'T/width:800,height:400,blur:1/IMG-URL'),
    ({'width': 800, 'height': 400, 'blur': 1}, 'T/width:800,height:400,blur:1/IMG-URL'),
    # Sharpen
    ({'width': 800, 'height': 400, 'sharpen': -1}, 'T/width:800,height:400,sharpen:1/IMG-URL'),
    ({'width': 800, 'height': 400, 'sharpen': 2}, 'T/width:800,height:400,sharpen:2/IMG-URL'),
    # File Extension
    ({'width': 800, 'height': 400, 'ext': Ext.GIF}, 'T/width:800,height:400,ext:gif/IMG-URL'),
    ({'width': 800, 'height': 400, 'ext': Ext.ICO}, 'T/width:800,height:400,ext:ico/IMG-URL'),
    ({'width': 800, 'height': 400, 'ext': Ext.JPEG}, 'T/width:800,height:400,ext:jpg/IMG-URL'),
    ({'width': 800, 'height': 400, 'ext': Ext.PNG}, 'T/width:800,height:400,ext:png/IMG-URL'),
    ({'width': 800, 'height': 400, 'ext': Ext.WEBP}, 'T/width:800,height:400,ext:webp/IMG-URL'),
])
def test_url(params, exp_url):
    res = url('IMG-URL', **params)

    exp_url_full = 'https://f1.bilder-fee.de/{0}'.format(exp_url)
    assert res == exp_url_full

