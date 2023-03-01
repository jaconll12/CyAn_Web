#!/bin/bash
#!/opt/homebrew/bin/
/opt/homebrew/bin/python3 -V
which python3
echo $PYTHONPATH
/opt/homebrew/bin/python3 -m pip install --upgrade pip
/opt/homebrew/bin/python3 -m pip install virtualenv
/opt/homebrew/bin/python3 -m virtualenv venv
source venv/bin/activate
/opt/homebrew/bin/python3 -m venv --upgrade ENV_DIR
PATH=/usr/local/mysql-8.0.32-macos13-arm64/bin:$PATH
export PATH
PYTHONPATH=/opt/homebrew/bin/python3
export PYTHONPATH
pip3 install --upgrade pip

python3 -V
pip3 install -r requirements.txt 
django-admin --version
/opt/homebrew/bin/python3 manage.py migrate
/opt/homebrew/bin/python3 manage.py test
deactivate
echo "build finished"