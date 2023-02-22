#!/bin/bash

echo "1"
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
export PATH=/usr/local/mysql-8.0.32-macos13-arm64/bin:$PATH 
echo "2"
pip3 install django
pip3 install django-sslserver
pip3 install djangorestframework
pip3 install PyMySQL
pip3 install mysqlclient
pip3 install mysql
pip3 install mysql-connector
pip3 install mysql-connector-python
pip3 install requests==2.27.1
pip3 install six==1.16.0
pip3 install threadpoolctl==3.1.0
pip3 install django_heroku
pip3 install gunicorn
pip3 install urllib3==1.26.9



django-admin --version
echo "3"



echo "3"
python3 manage.py migrate
python3 manage.py test
deactivate
echo "build finished"