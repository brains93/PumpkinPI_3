from flask import Flask, request, render_template, redirect, url_for
#from wireless import Wireless
#import connection as Finder
import requests
import subprocess
import os

app = Flask(__name__)

#sets up verables 
internet = ""
interfaces = []

#function to run shell commands
def runshell(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
 
@app.route('/')
def index():
    interfaces = os.listdir('/sys/class/net/')
    try: 
        requests.get("https://www.google.com")
        internet = "Internet connected"
    except:
        internet = "no internet connection"
    return render_template('index.html', internet=internet, interfaces=interfaces)

@app.route('/connect')
def connect():
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

@app.route('/start')
def startpumpkin(): 
    #sets up WiFi connection command 
    Command = f"wifipumpkin3"
    runshell(Command)
    #redirects back to main page 
    return redirect("/")

@app.route('/dashboard')
def dashboard(): 
    #sets up WiFi connection command 
    #Command = f"/home/grant/wifipumpkin3/wifipumpkin3"
    #runshell(Command)
    #redirects back to main page 
    return render_template('dashboard.html')