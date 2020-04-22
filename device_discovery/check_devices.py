#!/usr/bin/python3

import subprocess
import os
import json

#runs the bash script and records all of the outputs
dir_path = os.path.dirname(os.path.realpath(__file__))
devices = subprocess.run([dir_path + "/check_arp.sh"], stdout=subprocess.PIPE)
output = devices.stdout.decode()

#set a flag to differentiate between eth0 and wlan0 when collecting addr
isWlan = False
#create two lists that will hold our addr
macsEth0 = [] #Controller devices
macsWlan0 = [] #Controlled devices
#loop through the output and load up both lists with the addr
for line in output.split('\n'):
    dev = line.split(' ')
    #use $ character as a delimiter between the two types of addr
    if line == "$":
        #when $ is found flip the boolean to True
        isWlan = True
    if(len(dev) < 2):
            continue
    #If the $ character is not found load up the eth0 list
    if isWlan == False:
        macsEth0.append({"IPv4":dev[0], "MAC":dev[1]})
    #When the $ character is found load up the wlan0 list (excluding the $ character)
    elif line != '$':
        macsWlan0.append({"IPv4":dev[0], "MAC":dev[1]})

#Load Current JSON object
devices = {}

#Load up the json object
try:
    with open(dir_path + "/../assistop/myapp/documentation/JSON/devices.json", "r") as rfile:
        devices = json.load(rfile)
except:
    #Devices file failed. Assume non existent
    devices = {"controllerDevices" :[], "controlledDevices" : []}

#Ensure ethdev devices are updated within web
for ethdev in macsEth0:
    found = None
    for item in devices["controllerDevices"]:
        if item["MAC"] == ethdev["MAC"]:
            if item["IPv4"] != ethdev["IPv4"]:
                item["IPv4"] = ethdev["IPv4"]
            item["online"] = 1
            found = True
    if not found:
        devices["controllerDevices"].append({
            "UserName": "Unknown",
            "ModelName": "Unknown",
            "MAC": ethdev["MAC"],
            "IPv4": ethdev["IPv4"],
            "online": 1
            })
#Check for offline devices
for item in devices["controllerDevices"]:
    found = None
    for ethdev in macsEth0:
        if item["MAC"] == ethdev["MAC"]:
            found = True
            break
    if not found:
        item["online"] = 0

#Ensure wlan0 devices are updated within web
for wlandev in macsWlan0:
    found = None
    for item in devices["controlledDevices"]:
        if item["MAC"] == wlandev["MAC"]:
            if item["IPv4"] != wlandev["IPv4"]:
                item["IPv4"] = wlandev["IPv4"]
            item["online"] = 1
            found = True
    if not found:
        devices["controlledDevices"].append({
            "UserName": "Unknown",
            "ModelName": "Unknown",
            "MAC": wlandev["MAC"],
            "IPv4": wlandev["IPv4"],
            "online": 1
            })
#Check for offline devices
for item in devices["controlledDevices"]:
    found = None
    for wlandev in macsWlan0:
        if item["MAC"] == wlandev["MAC"]:
            found = True
            break
    if not found:
        item["online"] = 0

#Write to the JSON file
with open(dir_path + "/../assistop/myapp/documentation/JSON/devices.json", "w") as rfile:
    json.dump(devices, rfile)
