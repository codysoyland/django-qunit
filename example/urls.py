from django.conf.urls import *

urlpatterns = [
    url('^qunit/', include('django_qunit.urls'))
]
