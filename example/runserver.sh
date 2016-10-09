#!/bin/sh

PYTHONPATH=`pwd`:`pwd`/..:$PYTHONPATH
python manage.py runserver --settings=settings 8080
