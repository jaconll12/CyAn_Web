#!/bin/bash
#!/opt/homebrew/bin/python3
python3 -V
which python3

source cyan-env/bin/activate

PATH=/usr/local/mysql-8.0.32-macos13-arm64/bin:$PATH
PATH=/opt/homebrew/bin:$PATH
export PATH
PYTHONPATH=/opt/homebrew/bin/python3
export PYTHONPATH

python3 -V
django-admin --version

python3 manage.py runserver
deactivate
echo "test finished"
