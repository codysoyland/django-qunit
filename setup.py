#!/usr/bin/env python
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-qunit2',
    version='20130624',
    description='QUnit Javascript testing integration for Django.',
    long_description=README,
    author='Timothy Van Heest',
    author_email='timothy.vanheest@gmail.com',
    url='http://github.com/turtlemonvh/django-qunit/',
    packages=[
        'django_qunit',
    ],
    package_data={
        'django_qunit': ['templates/qunit/*', 'media/qunit/*'],
    },
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: JavaScript',
                 'Topic :: Software Development :: Testing'],
)
