#!/bin/bash
pip3 install virtualenv
echo "1"
virtualenv newenv
source newenv/bin/activate
pip3 install --upgrade pip
pip3 install django
pip3 install django-sslserver
pip3 install djangorestframework
pip3 install mysql-connector
pip3 install mysql-connector-python
pip3 install mysql-python
pip3 install requests==2.27.1
pip3 install six==1.16.0
pip3 install threadpoolctl==3.1.0
pip3 install django_heroku
pip3 install gunicorn
pip3 install urllib3==1.26.9


echo "2"
django-admin --version
echo "3"



echo "3"
python3 manage.py migrate
python3 manage.py test
deactivate
echo "build finished"