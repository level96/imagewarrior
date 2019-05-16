import pytest

from django.template import Template
from django.template import Context

from imagewarrior.django_compat.context_processors import imagewarrior


@pytest.mark.parametrize('tpl_tag, exp_url', [
    ('{% image_src "/IMG" "400x500" %}', 'T/width:400,height:500/my-hp.de/IMG'),
    # Gravity
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_SMART %}', 'T/width:400,height:500,gravity:sm/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_NORTH %}', 'T/width:400,height:500,gravity:no/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_SOUTH %}', 'T/width:400,height:500,gravity:so/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_EAST %}', 'T/width:400,height:500,gravity:ea/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_WEST %}', 'T/width:400,height:500,gravity:we/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_CENTER %}', 'T/width:400,height:500,gravity:ce/my-hp.de/IMG'),
    # DPR
    ('{% image_src "/IMG" "400x500" dpr=2 %}', 'T/width:400,height:500,dpr:2/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" dpr=1.5 %}', 'T/width:400,height:500,dpr:1.5/my-hp.de/IMG'),
    # Quality
    ('{% image_src "/IMG" "400x500" quality=0 %}', 'T/width:400,height:500,quality:50/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" quality=80 %}', 'T/width:400,height:500,quality:80/my-hp.de/IMG'),
    # Background
    ('{% image_src "/IMG" "400x500" background="abc" %}', 'T/width:400,height:500,background:abc/my-hp.de/IMG'),
    # Blur
    ('{% image_src "/IMG" "400x500" blur=0 %}', 'T/width:400,height:500,blur:1/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" blur=2 %}', 'T/width:400,height:500,blur:2/my-hp.de/IMG'),
    # Sharpen
    ('{% image_src "/IMG" "400x500" sharpen=0 %}', 'T/width:400,height:500,sharpen:1/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" sharpen=2 %}', 'T/width:400,height:500,sharpen:2/my-hp.de/IMG'),
    #  File extension
    ('{% image_src "/IMG" "400x500" ext=EXT_JPEG %}', 'T/width:400,height:500,ext:jpg/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" ext=EXT_PNG %}', 'T/width:400,height:500,ext:png/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" ext=EXT_GIF %}', 'T/width:400,height:500,ext:gif/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" ext=EXT_WEBP %}', 'T/width:400,height:500,ext:webp/my-hp.de/IMG'),
    ('{% image_src "/IMG" "400x500" ext=EXT_ICO %}', 'T/width:400,height:500,ext:ico/my-hp.de/IMG'),
])
def test_django_image_src(tpl_tag, exp_url):
    ctx = Context(imagewarrior(None))
    url = Template(
        '{% load imagewarrior %}' +
        tpl_tag
    ).render(context=ctx)

    exp_url_full = 'https://f1.bilder-fee.de/{0}'.format(exp_url)
    assert url == exp_url_full


def test_django_image_tag_calls_url(mocker):
    mock_image_url = mocker.patch('imagewarrior.django_compat.templatetags.imagewarrior.image_src')

    ctx = Context(imagewarrior(None))
    Template(
        '{% load imagewarrior %}'
        '{% image "/IMG" "400x500" %}'
    ).render(context=ctx)

    mock_image_url.assert_called_once_with('/IMG', '400x500')


@pytest.mark.parametrize('tpl_tag, exp_url', [
    ('{% image "/IMG" "400x500" %}', '<img class=" iw-lazy" data-src="I"/>'),
    ('{% image "/IMG" "400x500" id="ID" alt="A" %}', '<img id="ID" alt="A" class=" iw-lazy" data-src="I"/>'),
    ('{% image "/IMG" "400x500" id="ID" alt="A" class="cls cls2" %}',
     '<img id="ID" alt="A" class="cls cls2 iw-lazy" data-src="I"/>'),
    # Lazy
    ('{% image "/IMG" "400x500" lazy=False %}', '<img src="I"/>'),
    ('{% image "/IMG" "400x500" lazy=False id="ID" alt="A" %}', '<img id="ID" alt="A" src="I"/>'),
])
def test_django_image_tag_rendering(tpl_tag, exp_url):
    ctx = Context(imagewarrior(None))
    url = Template(
        '{% load imagewarrior %}' +
        tpl_tag
    ).render(context=ctx)

    url = url.replace('https://f1.bilder-fee.de/T/width:400,height:500/my-hp.de/IMG', 'I')

    assert url == exp_url
