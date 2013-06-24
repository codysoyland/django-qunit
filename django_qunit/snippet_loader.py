"""
Subclass of django.template.loaders.app_directories.Loader

For finding html snippet templates within app directories qunit folders.
"""

import os
import sys

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
from django.utils._os import safe_join
from django.utils import six
from django.template.loaders.app_directories import Loader as AppLoader

# At compile time, cache the directories to search.
if not six.PY3:
    fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
app_template_dirs = []
for app in settings.INSTALLED_APPS:
    try:
        mod = import_module(app)
    except ImportError as e:
        raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))
    template_dir = os.path.join(os.path.dirname(mod.__file__), "static", settings.QUNIT_TEST_PATH)
    if os.path.isdir(template_dir):
        if not six.PY3:
            template_dir = template_dir.decode(fs_encoding)
        app_template_dirs.append(template_dir)

class Loader(AppLoader):
    def get_template_sources(self, template_name, template_dirs=None):
        """
        Re-run this function with the new value of app_template_dirs
        """
        if not template_dirs:
            template_dirs = app_template_dirs
        for template_dir in template_dirs:
            try:
                yield safe_join(template_dir, template_name)
            except UnicodeDecodeError:
                # The template dir name was a bytestring that wasn't valid UTF-8.
                raise
            except ValueError:
                # The joined path was located outside of template_dir.
                pass
