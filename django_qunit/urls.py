from django.conf.urls.defaults import *
from django.conf import settings
import os
from views import run_tests

media_root = os.path.join(os.path.dirname(__file__), 'media')

urlpatterns = patterns('',
    url(r'^qunit/qunit.js', 'django.views.static.serve', {
        'document_root': media_root, 'path': 'qunit/qunit.js',
    }, name='qunit_js'),
    url(r'^qunit/qunit.css', 'django.views.static.serve', {
        'document_root': media_root, 'path': 'qunit/qunit.css',
    }, name='qunit_css'),
    url('^(?P<path>.*)$', run_tests,
        name='qunit_test_overview'),
)
