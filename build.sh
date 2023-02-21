#!/bin/bash

echo "1"

echo "2"
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "3"
python3 manage.py migrate
python3 manage.py test

echo "build finished"