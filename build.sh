#!/bin/bash

echo "1"
python3 -v
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
export PATH=/usr/local/mysql-8.0.32-macos13-arm64/bin:$PATH 
echo "2"
pip3 install -r requirements.txt 




django-admin --version
echo "3"



echo "3"
python3 manage.py migrate
python3 manage.py test
deactivate
echo "build finished"