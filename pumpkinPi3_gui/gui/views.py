from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
import subprocess
import os

#sets up verables 
internet = ""
interfaces = []

#function to run shell commands
def runshell(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def gui(request):
    interfaces = os.listdir('/sys/class/net/')
    try: 
        requests.get("https://www.google.com")
        internet = "Internet connected"
    except:
        internet = "no internet connection"
    return render(request, 'gui/index.html', {'internet': internet,'interfaces': interfaces })

def connect(request):
    #take input from the HTTP Get request and assigns it to a vaerable
    #Needs changed to Post requests 
    ssid = request.args.get("ssid")
    password = request.args.get("password")
    interface = request.args.get("interface")
    
    #sets up WiFi connection command 
    Command = f"/usr/bin/nmcli dev wifi connect {ssid} password {password} ifname {interface}"
    runshell(Command)
    #redirects back to main page 
    return redirect("/")

def dashboard(request):
    return render(request, 'gui/dashboard.html', {})