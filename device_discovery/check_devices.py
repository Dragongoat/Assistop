#!/usr/bin/python3

import subprocess

devices = subprocess.run(["./check_arp.sh"], stdout=subprocess.PIPE)
output = devices.stdout.decode()

macs = []
for line in output.split('\n'):
    dev = line.split(' ')
    if(len(dev) < 2):
        continue
    macs.append({"IPv4":dev[0], "MAC":dev[1]})

print(macs)
