import os
import subprocess
#from sunau import AUDIO_FILE_ENCODING_DOUBLE
import time
from pprint import pprint
from datetime import datetime
import sys
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import lxml.etree as etree 


import json
#import local_cleanup

#import create_config

tar = sys.argv[2]
scanner = sys.argv[1]
#os.system(" python create_config.py " +tar)
#with open('config1.json') as json_data:
#    d = json.load(json_data)
#    target = d["environment"]["target"]
#    print ("CyAn Start on ", target)
#    print ("Starting Threadfix Docker Image")
#    docker_start_threadfix
#    import createin
#    createin
    ## Text menu in Python
print (scanner)
def print_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Burp")
    print ("2. Nessus")
    print ("3. Zap") 
    print ("4. All")
    print ("5. Exit")
    print (67 * "-")
    

def niktoscan(url):
    results = subprocess.getoutput("perl ../nikto/program/nikto.pl -nossl -h " +str(url))
    print(url)
    file = open("CyAn/output/nikto_out_" +str(url) + ".txt", "w")
    file.write(results)
    file.close
    return results

def wpscan(url):
    with open('/Users/jamesclloyd/CyAn_Web/scanner_config.json') as json_data:
        d = json.load(json_data)
    wpapikey = d["wpscan"]["wpapikey"]
    results = subprocess.getoutput("/opt/homebrew/bin/wpscan --api-token " +str(wpapikey)+ " --url " +str(url)+ " --ignore-main-redirect --disable-tls-checks -f json")
    filen = "CyAn/output/wpscan_" +str(url)+ ".json"
    json_string = json.dumps(results)
    with open(filen, 'w') as outfile:
        json.dump(json_string, outfile)
    print(url) 
    return results

def nmapscan(url):
    #print(os.system("pwd"))
    results = subprocess.check_output("nmap -sV -sC --script http-enum,http-headers,http-methods " +str(url) + " -oX CyAn/output/nmap_out_" +str(url) + ".xml", shell=True)
    print(url)
    return results
   
def zapscan(url):
    print  ("Zap scan started, XML Findings are on Output Directory")
    createconfig(url)
    #results = subprocess.getoutput("docker run -t owasp/zap2docker-stable zap-full-scan.py -t" +str(tar))
    subprocess.getoutput("python3 /Users/jamesclloyd/CyAn_Web/CyAn/scripts/zap_api.py")
    x = etree.parse('/Users/jamesclloyd/CyAn_Web/CyAn/output/zap_report_' +str(url)+ '.xml') 
    xfile = etree.tostring(x, pretty_print = True)
    #return results
    return xfile

    
def createconfig(url):
    tar = "http://" + url
    data = {}
    data ['target'] = []
    data['target'].append({
    'URL': tar,
    'hostname': url
    })
    with open('CyAn/scripts/config1.json', 'w') as json_data:
        json.dump(data, json_data, indent=4)
        json_data.close()


def write_db(url,nmapresults,niktoresults,zapresults,wpresults):
    with open('db.json') as json_data:
        d = json.load(json_data)
        for p in d['db']:
            datab = p["database"]
            host = p["host"]
            user = p["user"]
            password = p["password"] 

    #json_file = "/Users/jamesclloyd/CyAn_Web/CyAn/output/wpscan_" +str(url)+ ".json"
    #with open(json_file, 'r') as myfile:
    #    wpscanresults=myfile.read()
    
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    try:
        connection = mysql.connector.connect(host = host,
                                         port = "3306",
                                         database = datab,
                                         user= user,
                                         password = password,
                                         auth_plugin='mysql_native_password')
        mySql_insert_query = """INSERT INTO findings (url,nmap_results, nikto_results, zap_results, wpscan_results, date_ran) VALUES (%s,%s,%s,%s,%s,%s) """,(url,nmapresults, niktoresults, zapresults,wpresults, formatted_date)
        cursor = connection.cursor()
        cursor.execute(*mySql_insert_query)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Findings Database")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Findings Database {}".format(error))

    #finally:
        #if (connection.is_connected()):
        #    connection.close()
        #    print("MySQL connection is closed")


def closeup(url):
    today = datetime.now()
    folder = today.strftime('%Y%m%d') +"_" +str(url)
    if not os.path.exists("CyAn/" + folder):
        os.system("mkdir CyAn/" +folder)
        os.system("cp -rf CyAn/output/* CyAn/" + folder)
        os.system("rm -rf CyAn/output/*")
    else:
        os.system("cp -rf CyAn/output/* CyAn/" + folder)
        os.system("rm -rf CyAn/output/*")

createconfig(tar)
nmapr = "NULL"
niktor = "NULL"
zapr = "NULL"
wptor = "NULL"
if scanner == "nmap":
    nmapr = nmapscan(tar)
elif scanner== "zap":
    zapr = zapscan(tar)
elif scanner== "nikto":
    niktor= niktoscan(tar)
elif scanner== "wpscan":
    wptor= wpscan(tar)
elif scanner=="all":
    nmapr = nmapscan(tar)
    niktor= niktoscan(tar)
    zapr = zapscan(tar)
else:
    print ("You must choose a scanner. nmap,zap,nikto,wpscan or all {'all' does not include WPScan}")
write_db(tar, nmapr, niktor, zapr, wptor)
closeup(tar)