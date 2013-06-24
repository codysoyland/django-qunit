import os

BASE_PATH = os.path.dirname(__file__)

QUNIT_TEST_PATH = os.path.join(BASE_PATH, 'qunit')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'example.urls'

INSTALLED_APPS = (
    'django_qunit',
)
