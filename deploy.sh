#!/bin/bash
python3 -m venv env
python3 -m pip install --upgrade pip
echo $PWD
source env/bin/activate

python3 manage.py runserver 

echo "server running"