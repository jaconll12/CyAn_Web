#!/bin/bash
#!/opt/homebrew/bin/python3
echo "1"
python3 -V
which python3
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
echo "2"
pip3 install -r requirements.txt 



django-admin --version
echo "3"



echo "3"
python3 manage.py migrate
python3 manage.py test
deactivate
echo "build finished"