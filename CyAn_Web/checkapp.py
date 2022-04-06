#check file.py

import sys
from django.urls import resolve

#app_name = sys.modules[resolve(request.path_info).func.__module__].__package__

print (__package__)