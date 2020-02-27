from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json,requests
from subprocess import Popen, PIPE, STDOUT



def cyan_nmap(target):

        command = ["python","CyAn/scripts/cyan_small.py","nmap",target]
        try:
                process = Popen(command, stdout=PIPE, stderr=STDOUT)
                #output = "Burp was selected"
                #output = "Scanning URL" %cho
                output = process.stdout.read()
                outp = "NMAP Scan finished and exported to XML file"
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
                outp = "ZAP Scan finished and exported to XML file"
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
                        data = cyan_nmap(url)
                elif request_data["scanner"] == "zap":
                        data = cyan_zap(url)
                else:
                        data = {"status": "not defined", "output":"not defined"}

                
                response = HttpResponse(json.dumps(data) , content_type='application/json', status=200)
                return response
        elif request.method == 'GET':
                scanner = request.GET['scanner']
                url = request.GET['url']
                if scanner == "nmap":
                        data = cyan_nmap(url)
                elif scanner == "zap":
                        data = cyan_zap(url)
                else:
                        data = {"status": "not defined", "output":"not defined"}
                
                response = HttpResponse(json.dumps(data) , content_type='application/json', status=200)
                return response
                #return HttpResponse('<h2>GET Worked. Scanner is {}, and the URL to be scanned it {}</h2>'.format(scanner,url))