#!/bin/bash

pip3 install virtualenv
echo "1"
virtualenv env
source env/bin/activate
echo "2"
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "3"
python3.10 manage.py migrate
python3.10 manage.py test

echo "build finished"