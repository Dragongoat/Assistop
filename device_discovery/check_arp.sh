#!/bin/bash

nmap -sn 10.0.0.0/24 &>/dev/null

arp -a &>/dev/null
arp -a -i eth0 | awk '{if($4 != "<incomplete>"){print (substr($2, 2, length($2)-2), $4)}}'
