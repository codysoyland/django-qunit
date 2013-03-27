django-qunit
============

django-qunit integrates the [QUnit Javascript testing framework][1] with
[Django][2], making it possible to run QUnit tests alongside your Django
app and test Ajax routines.

  [1]: http://docs.jquery.com/QUnit
  [2]: http://www.djangoproject.com/

Installation
============

 1. Add `django_qunit` to your `settings.INSTALLED_APPS`.
 2. Add `settings.QUNIT_TEST_DIRECTORY`, containing the path to your javascript files.
 3. Add a urlconf to `include('django_qunit.urls')`.

  If you would only like these urls available in debug mode, use something like the following.

        if settings.DEBUG:
            """Test-only urls """
            urlpatterns += patterns('',
                (r'^qunit/', include('django_qunit.urls')),
            )  
 
 4. Visit the URL you've included in your urlconf, and it should display QUnit test results.

*See the example in the tarball for more information.*

Configuration
==============
* Qunit test directory layout

  Extending upon the contents of the `examples` directory, we found something resembling the following works well, assuming `qunit_tests` is your base directory. 
  Group tests into files then folders.  Folders can be nested.

        * qunit_tests
            * section_a
                * test1.js
                * test2.js
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

License
=======
Copyright (c) 2010 Cody Soyland

Licensed new-style BSD, also containing QUnit, which is licensed MIT. See LICENSE file for more information.
