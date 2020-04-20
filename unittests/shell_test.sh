#!/bin/bash


#After some research, I can't find a decent framework to test shell scripts. It's probably best to attempt to do a unit test for my own sanity's sake and move on


#Shell Scripts:
#install.sh -- Will completely wipe the system. So in doing this, it will potentially break
#more than it will have shown breaking. This will require manual testing

#runSSH.hs -- Has to be run by a python script inside a shell script. Will manually test


#ToggleDevices.sh
ip=`ip addr show eth0 | grep -Po "inet \d+\.\d+\.\d+\.\d+" | sed "s/inet //"`
gateway=`ip route | grep default | grep -Po -m 1 "\d+\.\d+\.\d+\.\d+" | head -1`

#block communications with the gateway

../device_discovery/toggleDevices.sh $gateway A
ping $gateway -w 3 || echo "toggleDevices.sh Failed to stop communications with gateway"
../device_discovery/toggleDevices.sh $gateway D
ping $gateway -w 3 || echo "toggleDevices.sh Failed to restart communications with gateway"
