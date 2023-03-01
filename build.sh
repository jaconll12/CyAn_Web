#!/bin/bash
#!/opt/homebrew/bin/
/opt/homebrew/bin/python3 -V
which python3
echo $PYTHONPATH
/opt/homebrew/bin/python3 -m pip install --upgrade pip
/opt/homebrew/bin/python3 -m pip install virtualenv



/opt/homebrew/bin/python3 -m virtualenv cyan-env
source yan-env/bin/activate

PATH=/usr/local/mysql-8.0.32-macos13-arm64/bin:$PATH
PATH=/opt/homebrew/bin:$PATH
export PATH
PYTHONPATH=/opt/homebrew/bin/python3
export PYTHONPATH
pip3 install --upgrade pip

python3 -V
/opt/homebrew/bin/python3 -m pip install -r requirements.txt 
/opt/homebrew/bin/python3 -m pip install django
django-admin --version


echo "build finished"