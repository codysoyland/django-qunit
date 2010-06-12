#!/usr/bin/env python
from distutils.core import setup

setup(
    name='django-qunit',
    version='0.1.1',
    description='QUnit Javascript testing integration for Django.',
    long_description=open('README.md').read(),
    author='Cody Soyland',
    author_email='codysoyland@gmail.com',
    url='http://github.com/codysoyland/django-qunit/',
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
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: JavaScript',
                 'Topic :: Software Development :: Testing'],
)
