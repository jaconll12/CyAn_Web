import os
import subprocess
import time
from pprint import pprint
import sys
#import nessus_scan
#import docker_start_threadfix
import json
#import local_cleanup
import sys 
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
    
def menu():
    loop=True      
  
    while loop:          ## While loop which will keep going until loop = False
        print_menu()    ## Displays menu
        choice = input("Enter your choice [1-5]: ")
        if choice == "1":     
            answer = "burp"
            print  ("Burp was selected")
            print (answer)
            loop=False
        elif choice=="2":
            answer = "NMAP"
            print  ("NMAP was selected")
            print (answer)
            loop=False
        elif choice=="3":
            answer = "zap"
            print  ("Zap was selected")
            print (answer)
            loop=False
        elif choice=="4":
            answer = "all"
            print  ("All Scanners was selected")
            print (answer)
            loop=False
        elif choice=="5":
            answer = "exit"
            print  ("Exiting")
            sys.exit()
            break
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")
    return (answer)
def nmapscan(url):
    os.system("nmap -sV --script http-enum " +str(url) + " -oX Cyan/output/out.xml")
    print(url)
def zapscan(url):
    print  ("Zap scan started")
    os.system("python /Users/jamesclloyd/CyAn_Web/CyAn/scripts/zap_api.py")
    #import threadfix_upload_ZAP
    #threadfix_upload_ZAP
    #print ("ZAP Scan Uploaded")

def createconfig(url):
    #tar = sys.argv[0]
    tar = url
    data = {}
    data ['target'] = []
    data['target'].append({
    'URL': tar
    })
    with open('config1.json', 'w') as json_data:
        json.dump(data, json_data, indent=4)
        json_data.close()


#answer = menu()
createconfig(tar)
#print ("This is the option: " + answer)
if scanner == "nmap":
    nmapscan(tar)
elif scanner== "zap":
    zapscan(tar)



