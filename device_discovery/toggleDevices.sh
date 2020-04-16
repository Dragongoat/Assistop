#!/bin/bash
#-----------------begin script------------------#
# $1 - What IP address we will be toggling
# $2 - Whether or not we want to turn the IP address on or off: "D" for turn this thing off. "A" for turn this thing on.
sudo iptables -$2 INPUT -s $1 -j DROP  
