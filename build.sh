#!/bin/bash
#!/opt/homebrew/bin/python3
echo "1"
python3 -V
which python3
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
python3 -m venv --upgrade ENV_DIR
pip3 install --upgrade pip
PATH=/usr/local/mysql-8.0.32-macos13-arm64/bin:$PATH
export PATH
PYTHONPATH=/opt/homebrew/bin/python3
export PYTHONPATH
echo "2"
python3 -V
pip3 install -r requirements.txt 



django-admin --version
echo "3"



echo "3"
python3 manage.py migrate
python3 manage.py test
deactivate
echo "build finished"