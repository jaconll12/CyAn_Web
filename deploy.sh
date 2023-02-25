#!/bin/bash
#!/opt/homebrew/bin/python3
python3 -V
which python3
source venv/bin/activate
django-admin --version
python3 manage.py runserver
deactivate
echo "test finished"
