import os
import subprocess
import time
from pprint import pprint
from datetime import datetime
import sys
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


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
    results = subprocess.check_output("nikto -h " +str(url)+ " -output CyAn/output/nikto_"+str(url) + ".txt", shell=True)
    print(url)
    return results
     
def nmapscan(url):
    results = subprocess.check_output("nmap -sV -sC --script http-enum,http-headers,http-methods " +str(url) + " -oX CyAn/output/nmap_out_" +str(url) + ".xml", shell=True)
    print(url)
    return results
   
def zapscan(url):
    print  ("Zap scan started")
    createconfig(url)
    results = subprocess.check_output("python CyAn/scripts/zap_api.py", shell=True)
    return results

    
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


def write_db(url,nmapresults,niktoresults,zapresults):
    with open('../db.json') as json_data:
        d = json.load(json_data)
        for p in d['db']:
            db = p["database"]
            host = p["host"]
            user = p["user"]
            password = p["password"] 


    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    try:
        connection = mysql.connector.connect(host=host,
                                         database=db,
                                         user=user,
                                         password=password,
                                         auth_plugin='mysql_native_password')
        mySql_insert_query = """INSERT INTO findings (url,nmap_results, nikto_results, zap_results, date_ran) VALUES (%s,%s,%s,%s,%s) """,(url,nmapresults, niktoresults, zapresults, formatted_date)
        cursor = connection.cursor()
        cursor.execute(*mySql_insert_query)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Findings Database")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Findings Database {}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")


def closeup(url):
    today = datetime.now()
    folder = today.strftime('%Y%m%d') +"_" +str(url)
    if not os.path.exists("CyAn/" + folder):
        os.makedirs("CyAn/" + folder)
        #os.mkdir("CyAn/" + folder)
    os.system("cp -rf CyAn/output/* CyAn/" + folder)
    os.system("rm CyAn/output/*")


createconfig(tar)
nmapr = "NULL"
niktor = "NULL"
zapr = "NULL"
if scanner == "nmap":
    nmapr = nmapscan(tar)
elif scanner== "zap":
    zapr = zapscan(tar)
elif scanner== "nikto":
    niktor= niktoscan(tar)

write_db(tar, nmapr, niktor, zapr)
closeup(tar)



