#!/bin/bash
/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip
echo "1"
/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install virtualenv
virtualenv env -p python3
source env/bin/activate
echo "2"
env/bin/pip3 install --upgrade pip
env/bin/pip3 install -r requirements.txt

echo "3"
env/bin/python3 manage.py migrate
env/bin/python3 manage.py test

echo "build finished"