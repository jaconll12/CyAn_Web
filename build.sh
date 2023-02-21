#!/bin/bash
pip3 install virtualenv
echo "1"
virtualenv newenv
source newenv/bin/activate

pip3 install django
pip3 install django-sslserver
pip3 install djangorestframework
echo "2"
django-admin --version
echo "3"
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "3"
python3 manage.py migrate
python3 manage.py test
deactivate
echo "build finished"