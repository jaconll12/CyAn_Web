#!/bin/bash
apt install python3-dev default-libmysqlclient-dev build-essential
echo "down to pip"
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install django
pip install django-sslserver
pip install djangorestframework
pip install mysql==0.0.3
pip install mysql-connector==2.2.9
pip install mysql-connector-python==8.0.28
pip install mysqlclient
#pip3 install django-sslserver
#pip install -r reqs.txt
echo $PWD

#python3 manage.py runsslserver 
python3 manage.py runserver 
source env/bin/deactivate
echo "server running"

