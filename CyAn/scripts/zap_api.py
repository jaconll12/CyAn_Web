#!/usr/bin/env python
import requests
import sys
import traceback
import shutil
import time
from pprint import pprint
import os
import subprocess
import json
#from zapv2 import ZAPV2
from zapv2 import ZAPv2

with open('/Users/jamesclloyd/CyAn_Web/scanner_config.json') as json_data:
    d = json.load(json_data)
#target = d["zap"]["host"]
apikey = d["zap"]["api_key"]
with open('/Users/jamesclloyd/CyAn_Web/CyAn/scripts/config1.json') as json_data:
    d = json.load(json_data)
    for p in d['target']:
        target = p["URL"]
        hostname = p["hostname"]

print ('Starting ZAP ...')
#subprocess.Popen(['/home/zap/ZAP_2.9.0/zap.sh','-daemon'],stdout=open(os.devnull,'w'))
subprocess.Popen(['/Applications/OWASP ZAP.app/Contents/Java/zap.sh', '-daemon'],stdout=open(os.devnull,'w'))
print ('Waiting for ZAP to load, 20 seconds ...') 
time.sleep(20)

#apikey = "6mg88525c4049m0bfumg0f44mh" # Change to match the API key set in ZAP, or use None if the API key is disabled

# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apikey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
#zap = ZAPv2(apikey=apikey, proxies={'http': 'http://localhost:8080', 'https': 'http://localhost:8080'})
#print ("got the info")
# do stuff
print ('Accessing target %s' % target)
# try have a unique enough session...
zap.urlopen(target)
print ("past open target")
# Give the sites tree a chance to get updated
time.sleep(5)

print ('Spidering target %s' % target)
#print ("past spider target")
scanid = zap.spider.scan(target)
#scanid = zap.spider.scan(url=target, maxchildren=5, recurse = True, subtreeonly = False, apikey=apikey)
#print ("past spider2 target")
# Give the Spider a chance to start
time.sleep(2)
while (int(zap.spider.status(scanid)) < 100):
    print ('Spider progress %: ' + zap.spider.status(scanid))
    time.sleep(2)

print ('Spider completed')
# Give the passive scanner a chance to finish
time.sleep(5)

print ('Scanning target %s' % target)
scanid = zap.ascan.scan(target)
while (int(zap.ascan.status(scanid)) < 100):
    print ('Scan progress %: ' + zap.ascan.status(scanid))
    time.sleep(5)

print ('Scan completed')

# Report the results

#print ('Hosts: ' + ', '.join(zap.core.hosts))
#print ('Alerts: ')
#print (zap.core.alerts())

report_type = 'xml'
report_file = '/Users/jamesclloyd/CyAn_Web/CyAn/output/zap_report_' +str(hostname) + '.xml'
with open(report_file, 'w') as f:
    xml = zap.core.xmlreport()
    f.write(xml)
    print('Success: {1} report saved to {0}'.format(report_file, report_type.upper()))

#zap.core.xmlreport()
# To close ZAP:
zap.core.shutdown()
