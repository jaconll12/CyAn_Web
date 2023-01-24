#!/bin/bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install django
pip install -r reqs.txt
echo $PWD
source env/bin/activate

python3 manage.py runsslserver 
echo "server running"
