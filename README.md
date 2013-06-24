django-qunit
============

django-qunit integrates the [QUnit Javascript testing framework][1] with
[Django][2], making it possible to run QUnit tests alongside your Django
app and test Ajax routines.

  [1]: http://docs.jquery.com/QUnit
  [2]: http://www.djangoproject.com/

Installation
============

 1. Either: 
   * Install via `pip install [django_qunit2](https://pypi.python.org/pypi/django-qunit2/20130624)`
   * Download the files / clone the repo and put the `django_qunit/django_qunit` folder where ever you put your projects apps
 1. Add `django_qunit` (or `apps.django_qunit`, depending on which option you chose for the first step) to your `settings.INSTALLED_APPS`.
 2. Add `'django_qunit.snippet_loader.Loader',` to `settings.TEMPLATE_LOADERS`.
 3. Add `settings.QUNIT_TEST_PATH`, containing the path to the qunit test directory from within each app's static files directory, and your main project static directory.  This is a file path, so make sure to use `os.path.join` to create the path.
 
   For example, if `STATICFILES_DIRS` contains `"/path/to/my/project/static"` and `QUNIT_TEST_PATH` is `"qunit"`, place your test files inside a "qunit" folder in `os.path.join("/path/to/my/project/static", QUNIT_TEST_PATH)`. 
   Within each app, you should put the files in `appname/static_dir/QUNIT_TEST_PATH/appname/`.  Adding in `appname` keeps tests namespaced and creates a natural tree structure for your tests.
 
 4. Add a urlconf to `include('django_qunit.urls')`.

  If you would only like these urls available in debug mode, use something like the following in your base `urls.py` file.

        if settings.DEBUG:
            """Test-only urls """
            urlpatterns += patterns('',
                (r'^qunit/', include('django_qunit.urls')),
            )  
 
 5. Visit the URL you've included in your urlconf, and it should display QUnit test results.

Configuration
==============
* Qunit test directory layout

  Extending upon the contents of the `examples` directory, we found something resembling the following works well, assuming `qunit` is your QUNIT_TEST_PATH. 
  Group tests into files then folders.  Folders can be nested.

        * qunit
            * section_a
                * test1.js
                * test2.js
                * stub_a.html
                * suite.json
            * section_b
                * section_b1
                    * test1.js
                * test1.js
                * suite.json
            * section_c
                * test1.js
            * test1.js
            * suite.json

  Within an app, first create a empty folder with the name of the app, then add more tests and test directories with that.

        * qunit
            * myapp
                * test1.js
                * test2.js
                * stub1.html
                * suite.json
                * section_a
                    * section_b1
                        * test1.js
                    * test3.js
                    * suite.json
                * section_b
                    * test4.js
  
* Test configuration files

  Add a file named `suite.json` to any directory in `QUNIT_TEST_DIRECTORY` to change the displayed name of that testing directory 
  or change what external assets are loaded on that test page. For example, the following will load 
  the js files at the listed urls into the page `django-qunit` creates for the folder containing this configuration file.
  
  You can also pass an array named `extra_media_urls`, and these urls will be concatenated with your project's value of `settings.MEDIA_URL`.

        {
            "extra_urls": [
              "/static_assets/js/lib/jquery.js",
              "/static_assets/js/lib/underscore.js",
              "/static_assets/js/lib/jquery-ui.js"
            ]
        }
  
  Note that `suite.json` attributes are not inherited by lower level directories, so you need to define `suite.json` files for each 
  folder that needs additional assets loaded.
  
  Additionally, you can include `.html` files in any testing directory.  The contents of each of these files will be included on that 
  directory's testing page inside a `div` with an id determined by the name of the file.  For example, for the example stuctur above, 
  `stub_a.html` would be included in a `div` with id `stub_a`.  All html stubs are wrapped in a `div` with id `qunit-html-stubs`, and 
  this `div` is given the css property `display: none`.

License
=======
Copyright (c) 2012 Timothy Van Heest

Originally based off a fork of Cody Soyland's [django-qunit](https://github.com/codysoyland/django-qunit).

Licensed MIT, also containing QUnit, which is licensed MIT. See LICENSE file for more information.
