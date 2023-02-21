#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip3 install -r requirements.txt

python manage.py migrate
python manage.py test

echo "build finished"