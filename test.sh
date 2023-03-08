#!/bin/bash
#!/opt/homebrew/bin/
/opt/homebrew/bin/python3 -V
which python3

source cyan-env/bin/activate

PATH=/usr/local/mysql-8.0.32-macos13-arm64/bin:$PATH
PATH=/opt/homebrew/bin:$PATH
export PATH
PYTHONPATH=/opt/homebrew/bin/python3
export PYTHONPATH

python3 -V
django-admin --version
/opt/homebrew/bin/python3 -m pip install django
/opt/homebrew/bin/python3 manage.py migrate
/opt/homebrew/bin/python3 manage.py test
deactivate





echo "test finished"