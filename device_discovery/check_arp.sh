#!/bin/bash

# Get the subnets of eth0 and wlan0
eth0=$(ip address | grep eth0: -A2 | grep inet | awk '{print $2}')
wlan0=$(ip address | grep wlan0: -A2 | grep inet | awk '{print $2}')

# run nmap on eth0 network to populate arp table
nmap -sn $eth0 &>/dev/null
# wait for entries to be fully updated
sleep 4
# list arp table entries
ip neighbor list nud reachable dev eth0 | awk '{printf "%s %s\n", $1, $3}'

# insert a delimiter to indicate wlan0
echo $

# run nmap on wlan0 network to populate arp table
nmap -sn $wlan0 &>/dev/null
# wait for entries to be fully updated
sleep 4
# list arp table entries
ip neighbor list nud reachable dev wlan0 | awk '{printf "%s %s\n", $1, $3}'
