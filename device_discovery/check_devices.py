#!/usr/bin/python3

import subprocess

#runs the bash script and records all of the outputs
devices = subprocess.run(["./check_arp.sh"], stdout=subprocess.PIPE)
output = devices.stdout.decode()

#set a flag to differentiate between eth0 and wlan0 when collecting addr
isWlan = False;
#create two lists that will hold our addr
macsEth0 = []
macsWlan0 = []
#loop through the output and load up both lists with the addr
for line in output.split('\n'):
    dev = line.split(' ')
   #use $ character as a delimiter between the two types of addr
   if line == "$":
        #when $ is found flip the boolean to True
        isWlan = True
    #If the $ character is not found load up the eth0 list
    if isWlan == False:
        if(len(dev) < 2):
            continue
        macsEth0.append({"IPv4":dev[0], "MAC":dev[1]})
    #When the $ character is found load up the wlan0 list (excluding the $ character)
    elif line != '$':
        if(len(dev) < 2):
            continue
        macsWlan0.append({"IPv4":dev[0], "MAC":dev[1]})

#output the contents of each of the lists
print(f"Eth0: {macsEth0}")
print(f"Wlan0: {macsWlan0}")
