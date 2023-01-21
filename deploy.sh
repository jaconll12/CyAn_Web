#!/bin/bash
python3 -m venv env
python3 pip install --upgrade pip
pip install django
pip install -r requirements.txt
echo $PWD
source env/bin/activate

python3 manage.py runserver 
echo "server running"
