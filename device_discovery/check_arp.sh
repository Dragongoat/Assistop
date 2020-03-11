#!/bin/bash

#run nmap to populate arp table
nmap -sn 10.0.0.0/24 &>/dev/null

#run arp and acquire all mac addresses on the eth0 network
arp -a &>/dev/null
arp -a -i eth0 | awk '{if($4 != "<incomplete>"){print (substr($2, 2, length($2)-2), $4)}}'

#insert a delimiter so the first program knows when we're on wlan0
echo $
#run arp and acquire all mac addresses on the wlan0 network
arp -a &>/dev/null
arp -a -i wlan0 | awk '{if($4 != "<incomplete>"){print (substr($2, 2, length($2)-2), $4)}}'
