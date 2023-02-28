#!/bin/bash
#!/opt/homebrew/bin/
/opt/homebrew/bin/python3 -V
which python3
source venv/bin/activate
django-admin --version
/opt/homebrew/bin/python3 manage.py migrate
/opt/homebrew/bin/python3 manage.py test
deactivate
echo "test finished"