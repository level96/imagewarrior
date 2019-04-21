#!/usr/bin/env python
# encoding: utf-8

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='imagewarrior',
    version='0.1.0',
    description='Django/Jinja2 Templatetags Imagewarrior.',
    url='https://developer.imagewarrior.de/',
    author='ImageWarrior',
    author_email='hello@imagewarrior.de',
    packages=find_packages(),
    tests_require=[
        'enum34',
        'pytest',
        'pytest-cov',
        'pytest-django',
        'pytest-mock'
    ],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Severside',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Multimedia :: Image',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
