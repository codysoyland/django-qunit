#!/bin/sh

PYTHONPATH=`pwd`:`pwd`/..:$PYTHONPATH
python -c "import webbrowser; webbrowser.open_new_tab('http://localhost:8080/qunit/')"
django-admin.py runserver --settings=settings 8080 
