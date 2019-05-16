import pytest

from django.template import Template
from django.template import Context

from imagewarrior.django_compat.context_processors import imagewarrior


@pytest.mark.parametrize('tpl_tag, exp_url', [
    ('{% image_src "/IMG" "400x500" %}', 'width:400,height:500/IMG'),
    # Gravity
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_SMART %}', 'width:400,height:500,gravity:sm/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_NORTH %}', 'width:400,height:500,gravity:no/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_SOUTH %}', 'width:400,height:500,gravity:so/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_EAST %}', 'width:400,height:500,gravity:ea/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_WEST %}', 'width:400,height:500,gravity:we/IMG'),
    ('{% image_src "/IMG" "400x500" gravity=GRAVITY_CENTER %}', 'width:400,height:500,gravity:ce/IMG'),
    # DPR
    ('{% image_src "/IMG" "400x500" dpr=2 %}', 'width:400,height:500,dpr:2/IMG'),
    ('{% image_src "/IMG" "400x500" dpr=1.5 %}', 'width:400,height:500,dpr:1.5/IMG'),
    # Quality
    ('{% image_src "/IMG" "400x500" quality=0 %}', 'width:400,height:500,quality:50/IMG'),
    ('{% image_src "/IMG" "400x500" quality=80 %}', 'width:400,height:500,quality:80/IMG'),
    # Background
    ('{% image_src "/IMG" "400x500" background="abc" %}', 'width:400,height:500,background:abc/IMG'),
    # Blur
    ('{% image_src "/IMG" "400x500" blur=0 %}', 'width:400,height:500,blur:1/IMG'),
    ('{% image_src "/IMG" "400x500" blur=2 %}', 'width:400,height:500,blur:2/IMG'),
    # Sharpen
    ('{% image_src "/IMG" "400x500" sharpen=0 %}', 'width:400,height:500,sharpen:1/IMG'),
    ('{% image_src "/IMG" "400x500" sharpen=2 %}', 'width:400,height:500,sharpen:2/IMG'),
    #  File extension
    ('{% image_src "/IMG" "400x500" ext=EXT_JPEG %}', 'width:400,height:500,ext:jpg/IMG'),
    ('{% image_src "/IMG" "400x500" ext=EXT_PNG %}', 'width:400,height:500,ext:png/IMG'),
    ('{% image_src "/IMG" "400x500" ext=EXT_GIF %}', 'width:400,height:500,ext:gif/IMG'),
    ('{% image_src "/IMG" "400x500" ext=EXT_WEBP %}', 'width:400,height:500,ext:webp/IMG'),
    ('{% image_src "/IMG" "400x500" ext=EXT_ICO %}', 'width:400,height:500,ext:ico/IMG'),
])
def test_django_image_src(tpl_tag, exp_url):
    ctx = Context(imagewarrior(None))
    url = Template(
        '{% load imagewarrior %}' +
        tpl_tag
    ).render(context=ctx)

    exp_url_full = 'https://f1.bilder-fee.de/BF_TOKEN/{0}'.format(exp_url)
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

    url = url.replace('https://f1.bilder-fee.de/BF_TOKEN/width:400,height:500/IMG', 'I')

    assert url == exp_url
