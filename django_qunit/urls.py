from django.conf.urls.defaults import *
from django.conf import settings
import os
from views import run_tests

urlpatterns = patterns('',
    url('^(?P<path>.*)$', run_tests,
        name='qunit_test_overview'),
)
