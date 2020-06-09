from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json,requests
import xml
from subprocess import Popen, PIPE, STDOUT



def cyan_nmap(target):

        command = ["python","CyAn/scripts/cyan_small.py","nmap",target]
        try:
                process = Popen(command, stdout=PIPE, stderr=STDOUT)
                #output = "Burp was selected"
                #output = "Scanning URL" %cho
                output = process.stdout.read()
                #output = "NMAP Scan finished and exported to XML file"
                exitstatus = process.poll()
                if (exitstatus==0):
                        return {"status": "Success", "output":str(output)}
                else:
                        return {"status": "Failed", "output":str(output)}
        except Exception as e:
                return {"status": "failed", "output":str(e)}

def cyan_zap(target):

        command = ["python","CyAn/scripts/cyan_small.py","zap",target]
        try:
                process = Popen(command, stdout=PIPE, stderr=STDOUT)
                #output = "Burp was selected"
                #output = "Scanning URL" %cho
                output = process.stdout.read()
                #output = "ZAP Scan finished and exported to XML file"
                exitstatus = process.poll()
                if (exitstatus==0):
                        return {"status": "Success", "output":str(output)}
                else:
                        return {"status": "Failed", "output":str(output)}
        except Exception as e:
                return {"status": "failed", "output":str(e)}
                

def cyan_nikto(target):

        command = ["python","CyAn/scripts/cyan_small.py","nikto",target]
        try:
                process = Popen(command, stdout=PIPE, stderr=STDOUT)
                #output = "Burp was selected"
                #output = "Scanning URL" %cho
                output = process.stdout.read()
                #output = "ZAP Scan finished and exported to XML file"
                exitstatus = process.poll()
                if (exitstatus==0):
                        return {"status": "Success", "output":str(output)}
                else:
                        return {"status": "Failed", "output":str(output)}
        except Exception as e:
                return {"status": "failed", "output":str(e)}


@csrf_exempt
def cyan(request):
        if request.method == 'POST':
                request_data=json.loads(request.body)
                #data = cyan_1()
                url = request_data["url"]
                if request_data["scanner"] == "nmap":
                        t_data = cyan_nmap(url)
                elif request_data["scanner"] == "zap":
                        t_data = cyan_zap(url)
                elif request_data["scanner"] == "nikto":
                        t_data = cyan_nikto(url)
                elif request_data["scanner"] == "all":
                        data1 = cyan_nmap(url)
                        data2 = cyan_zap(url)
                        data3 = cyan_nikto(url)
                        t_data = dict(data1.items() + data2.items() + data3.items())
                else:
                        t_data = {"status": "not defined", "output":"not defined"}

                
                response = HttpResponse(json.dumps(t_data) , content_type='application/json', status=200)
                return response

        elif request.method == 'GET':
                scanner = request.GET['scanner']
                url = request.GET['url']
                if scanner == "nmap":
                        t_data = cyan_nmap(url)
                elif scanner == "zap":
                        t_data = cyan_zap(url)
                elif scanner == "nikto":
                        t_data = cyan_nikto(url)
                elif scanner == "all":
                        t_data = cyan_nmap(url)
                        t_data = cyan_zap(url)
                        t_data = cyan_nikto(url)
                        #t_data = {}
                        #for d in (data2, data2, data3): t_data.update(d)
                        t_data = "Scan Completed agaist %s, using ZAP, NMAP, and Nikto.  Check Output folder for results" %url
                        
                else:
                        t_data = {"status": "not defined", "output":"not defined"}
              
                response = HttpResponse(json.dumps(t_data) , content_type='application/json', status=200)
                return response
                #return HttpResponse('<h2>GET Worked. Scanner is {}, and the URL to be scanned it {}</h2>'.format(scanner,url))