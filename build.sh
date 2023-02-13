#!/bin/bash

python3 -m venv env

echo $PWD
source env/bin/activate

pip3 install -r requirements.txt

echo "build finished"