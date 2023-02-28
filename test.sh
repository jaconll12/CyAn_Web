#!/bin/bash
#!/opt/homebrew/bin/
/opt/homebrew/bin/python3 -V
which python3
source venv/bin/activate

/opt/homebrew/bin/python3 -m venv --upgrade ENV_DIR
PATH=/usr/local/mysql-8.0.32-macos13-arm64/bin:$PATH
export PATH
PYTHONPATH=/opt/homebrew/bin/python3
export PYTHONPATH

/opt/homebrew/bin/python3 pip install django



django-admin --version
/opt/homebrew/bin/python3 manage.py migrate
/opt/homebrew/bin/python3 manage.py test
deactivate
echo "test finished"