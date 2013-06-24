from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

try:
    settings.QUNIT_TEST_PATH
except AttributeError:
    raise ImproperlyConfigured('Missing required setting QUNIT_TEST_PATH.')

try:
    settings.PROJECT_PATH
except AttributeError:
    raise ImproperlyConfigured('Missing required setting PROJECT_PATH.')