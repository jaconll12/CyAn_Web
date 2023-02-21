#!/bin/bash
pip3 install virtualenv
echo "1"
virtualenv newenv
source newenv/bin/activate
echo "2"
pip3 install django
django-admin --version
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "3"
python3 manage.py migrate
python3 manage.py test
deactivate
echo "build finished"