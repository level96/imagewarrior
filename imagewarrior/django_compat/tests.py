import pytest

from django.template import Template
from django.template import Context

from imagewarrior.django_compat.context_processors import imagewarrior


@pytest.mark.parametrize('tpl_tag, exp_url', [
    ('{% image_src "IMG" "400x500" %}', 'insecure/rs:fill:400:500:0/plain/IMG'),
    # Gravity
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_SMART %}', 'insecure/rs:fill:400:500:0/g:sm/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_NORTH %}', 'insecure/rs:fill:400:500:0/g:no/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_SOUTH %}', 'insecure/rs:fill:400:500:0/g:so/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_EAST %}', 'insecure/rs:fill:400:500:0/g:ea/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_WEST %}', 'insecure/rs:fill:400:500:0/g:we/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_CENTER %}', 'insecure/rs:fill:400:500:0/g:ce/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_NORTH_EAST %}', 'insecure/rs:fill:400:500:0/g:noea/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_NORTH_WEST %}', 'insecure/rs:fill:400:500:0/g:nowe/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_SOUTH_EAST %}', 'insecure/rs:fill:400:500:0/g:soea/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_SOUTH_WEST %}', 'insecure/rs:fill:400:500:0/g:sowe/plain/IMG'),
    ('{% image_src "IMG" "400x500" gravity=GRAVITY_FOCUS gravity_focus="10,11" %}',
     'insecure/rs:fill:400:500:0/g:fp:10:11/plain/IMG'),
    # DPR
    ('{% image_src "IMG" "400x500" dpr=2 %}', 'insecure/rs:fill:400:500:0/dpr:2/plain/IMG'),
    ('{% image_src "IMG" "400x500" dpr=1.5 %}', 'insecure/rs:fill:400:500:0/dpr:1.5/plain/IMG'),
    # Quality
    ('{% image_src "IMG" "400x500" quality=0 %}', 'insecure/rs:fill:400:500:0/plain/IMG'),
    ('{% image_src "IMG" "400x500" quality=80 %}', 'insecure/rs:fill:400:500:0/q:80/plain/IMG'),
    # Background
    ('{% image_src "IMG" "400x500" background="10,11,12" %}', 'insecure/rs:fill:400:500:0/bg:10:11:12/plain/IMG'),
    # Blur
    ('{% image_src "IMG" "400x500" blur=0 %}', 'insecure/rs:fill:400:500:0/plain/IMG'),
    ('{% image_src "IMG" "400x500" blur=2 %}', 'insecure/rs:fill:400:500:0/bl:2/plain/IMG'),
    # Sharpen
    ('{% image_src "IMG" "400x500" sharpen=0 %}', 'insecure/rs:fill:400:500:0/plain/IMG'),
    ('{% image_src "IMG" "400x500" sharpen=2 %}', 'insecure/rs:fill:400:500:0/sh:2/plain/IMG'),
    #  File extension
    ('{% image_src "IMG" "400x500" ext=EXT_JPEG %}', 'insecure/rs:fill:400:500:0/plain/IMG@jpg'),
    ('{% image_src "IMG" "400x500" ext=EXT_PNG %}', 'insecure/rs:fill:400:500:0/plain/IMG@png'),
    ('{% image_src "IMG" "400x500" ext=EXT_GIF %}', 'insecure/rs:fill:400:500:0/plain/IMG@gif'),
    ('{% image_src "IMG" "400x500" ext=EXT_WEBP %}', 'insecure/rs:fill:400:500:0/plain/IMG@webp'),
    ('{% image_src "IMG" "400x500" ext=EXT_ICO %}', 'insecure/rs:fill:400:500:0/plain/IMG@ico'),
])
def test_django_image_src(tpl_tag, exp_url):
    ctx = Context(imagewarrior(None))
    url = Template(
        '{% load imagewarrior %}' +
        tpl_tag
    ).render(context=ctx)

    exp_url_full = 'http://localhost:8080/{0}'.format(exp_url)
    assert url == exp_url_full


def test_django_image_tag_calls_url(mocker):
    mock_image_url = mocker.patch('django_compat.templatetags.imagewarrior.image_src')

    ctx = Context(imagewarrior(None))
    Template(
        '{% load imagewarrior %}'
        '{% image "IMG" "400x500" %}'
    ).render(context=ctx)

    mock_image_url.assert_called_once_with('IMG', '400x500')


@pytest.mark.parametrize('tpl_tag, exp_url', [
    ('{% image "IMG" "400x500" %}', '<img class=" iw-lazy" data-src="I"/>'),
    ('{% image "IMG" "400x500" id="ID" alt="A" %}', '<img id="ID" alt="A" class=" iw-lazy" data-src="I"/>'),
    ('{% image "IMG" "400x500" id="ID" alt="A" class="cls cls2" %}',
     '<img id="ID" alt="A" class="cls cls2 iw-lazy" data-src="I"/>'),
    # Lazy
    ('{% image "IMG" "400x500" lazy=False %}', '<img src="I"/>'),
    ('{% image "IMG" "400x500" lazy=False id="ID" alt="A" %}', '<img id="ID" alt="A" src="I"/>'),
])
def test_django_image_tag_rendering(tpl_tag, exp_url):
    ctx = Context(imagewarrior(None))
    url = Template(
        '{% load imagewarrior %}' +
        tpl_tag
    ).render(context=ctx)

    url = url.replace('http://localhost:8080/insecure/rs:fill:400:500:0/plain/IMG', 'I')
    assert url == exp_url
