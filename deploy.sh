#!/bin/bash
python3 -m venv env
python3 -m pip install --upgrade pip
python3 pip install django
echo $PWD
source env/bin/activate

python3 manage.py runserver 

echo "server running"