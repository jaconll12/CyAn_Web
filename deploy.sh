#!/bin/bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install django
pip install django-sslserver
pip install djangorestframework
pip install mysqlclient
#pip3 install django-sslserver
#pip install -r reqs.txt
echo $PWD

#python3 manage.py runsslserver 
python3 manage.py runserver 
source env/bin/deactivate
echo "server running"

