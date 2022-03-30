# CyAn_Web
Django Version of CyAN
Work in Progress but this is a web app version of the CyAn agigated web app scanner.  Runs on Django, working on the React Front end next.

Works with Curl 
Availabe Scanners Nikto,NAMP Web NSE Scripts, ZAP

Cyan_Web API guidance 

Start Django Server
- run python3 manage.py runserver From  CyAn_Web

EDIT: Added support for WPScan (will require your own WPScan API Key)

POST 
Using Curl
 curl -i -d '{"scanner":"nmap","url":"sharksec.net"}' http://127.0.0.1:8000/cyan_api

Get Using Browser
http://127.0.0.1:8000/cyan_api?scanner=nmap&url=www.google.com

Get using Curl
curl --request GET "http://127.0.0.1:8000/cyan_api?scanner=nmap&url=www.google.com


Results - Pulls all results from DB for URL 
http://127.0.0.1:8000/cyan_api/results?url=www.google.com

NEED TO DO 
- Front end
- Requirements file
- more scanners


