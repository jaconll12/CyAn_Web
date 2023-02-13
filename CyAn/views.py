from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json,requests
import xml
from subprocess import Popen, PIPE, STDOUT

def cyan_all(target):

        command = ["python3","CyAn/scripts/cyan_small.py","all",target]
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

def cyan_nmap(target):

        command = ["python3","CyAn/scripts/cyan_small.py","nmap",target]
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

        command = ["python3","CyAn/scripts/cyan_small.py","zap",target]
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

        command = ["python3","CyAn/scripts/cyan_small.py","nikto",target]
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
def cyan_wpscan(target):

        command = ["python3","CyAn/scripts/cyan_small.py","wpscan",target]
        try:
                process = Popen(command, stdout=PIPE, stderr=STDOUT)
                output = process.stdout.read()
                #output = "ZAP Scan finished and exported to XML file"
                exitstatus = process.poll()
                if (exitstatus==0):
                        return {"status": "Success", "output":str(output)}
                else:
                        return {"status": "Failed", "output":str(output)}
        except Exception as e:
                return {"status": "failed", "output":str(e)}


def search(target):
        command = ["python3","CyAn/scripts/search.py", target]
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
                elif request_data["scanner"] == "wpscan":
                        t_data = cyan_wpscan(url)
                elif request_data["scanner"] == "all":
                        t_data = cyan_all(url)
                else:
                        t_data = {"status": "not defined", "output":"not defined"}

                
                #response = HttpResponse(json.dumps(t_data) , content_type='application/json', status=200)
                #return response
                return JsonResponse(t_data)
        elif request.method == 'GET':
                scanner = request.GET['scanner']
                url = request.GET['url']
                if scanner == "nmap":
                        t_data = cyan_nmap(url)
                elif scanner == "zap":
                        t_data = cyan_zap(url)
                elif scanner == "nikto":
                        t_data = cyan_nikto(url)
                elif scanner == "wpscan":
                        t_data = cyan_wpscan(url)
                elif scanner == "all":
                        t_data = cyan_all(url)
                else:
                        t_data = {"status": "not defined", "output":"not defined"}
              
                #response = HttpResponse(json.dumps(t_data) , content_type='application/json', status=200)
                #return response
                #return JsonResponse(t_data)
                return JsonResponse((t_data), content_type='application/json', status=200)
                #return HttpResponse('<h2>GET Worked. Scanner is {}, and the URL to be scanned it {}</h2>'.format(scanner,url))\

def results(request):
        if request.method == 'POST':
                request_data=json.loads(request.body)
                #data = cyan_1()
                url = request_data["url"]
                t_data = search(url)
                #response = HttpResponse(json.dumps(t_data) , content_type='application/json', status=200)
                #return response
                return JsonResponse(t_data)
        elif request.method == 'GET':
                #scanner = request.GET['scanner']
                url = request.GET['url']
                t_data = search(url)
        
                #response = HttpResponse(json.dumps(t_data) , content_type='application/json', status=200)
                #return response
                return JsonResponse((t_data), content_type='application/json', status=200)
