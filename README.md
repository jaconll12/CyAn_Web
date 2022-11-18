# CyAn_Web


adding test to see if Jenkins works. 


Latest Updates:
- moved to MYSQL DB
- added test cases 
- added wpscan as a scanner (need your own API Key)


Django Version of CyAN
Work in Progress but this is a web app version of the CyAn agigated web app scanner.  Runs on Django, working on the React Front end next.

Works with Curl 
Availabe Scanners Nikto,NAMP Web NSE Scripts, ZAP, and WPScan
Cyan_Web API guidance 

Start Django Server
- run python3 manage.py runserver From  CyAn_Web

- can run 3 scanners, nmap, nikto, and zap by using the scanner=all (this does not run wpscan)

POST 
Using Curl
 curl -i -d '{"scanner":"nmap","url":"sharksec.net"}' http://127.0.0.1:8000/cyan_api

Get Using Browser
http://127.0.0.1:8000/cyan_api?scanner=wpscan&url=www.google.com


Get using Curl
curl --request GET "http://127.0.0.1:8000/cyan_api?scanner=nmap&url=www.google.com


Results - Pulls all results from DB for URL 
http://127.0.0.1:8000/cyan_api/results/by_url?url=www.google.com

NEED TO DO 
- Front end
- Locking down Django App
- Burp Scanner
