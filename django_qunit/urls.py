from django.conf.urls import *
from django.conf import settings

from django.views.static import serve
from django_qunit import views

import os

media_root = os.path.join(os.path.dirname(__file__), 'media')

urlpatterns = [
    url(r'^tests/(?P<path>.*)$', serve, { 'document_root': settings.QUNIT_TEST_DIRECTORY, }, name='qunit_test'),
    url(r'^qunit/qunit.js', serve, { 'document_root': media_root, 'path': 'qunit/qunit.js', }, name='qunit_js'),
    url(r'^qunit/qunit.css', serve, { 'document_root': media_root, 'path': 'qunit/qunit.css',}, name='qunit_css'),
    url('^(?P<path>.*)$', views.run_tests, name='qunit_test_overview'),
]
