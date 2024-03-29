"""CyAn_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.conf.urls import re_path
from django.urls import path, re_path
from CyAn.views import cyan  #added
from CyAn.views import results 
#from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^cyan_api$', cyan, name='cyan'),
    re_path(r'^cyan_api/results/by_url$', results, name='results')
    #path('cyan_api/token', obtain_auth_token, name="auth_token")
    #url(r'^admin/', admin.site.urls),
    #url(r'^cyan_api$', cyan),
    #url(r'^cyan_api/results$', results)
    #path('cyan_api/<str:scanner>/', cyan)

    ]
