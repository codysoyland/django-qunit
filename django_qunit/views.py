from django.shortcuts import render_to_response
from django.conf import settings

import os

def run_tests(request):
    files = [file for file \
             in os.listdir(settings.QUNIT_TEST_DIRECTORY) \
             if file.endswith('.js')]
    return render_to_response('qunit/index.html', {'files': files})
