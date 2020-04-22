#!/usr/bin/expect -f

set device [lindex $argv 0]

set toggle [lindex $argv 1]

# SSH's into the host pi and runs the deviceToggle.sh script
spawn ssh -l pi 192.168.1.99 -p 2112 "~/Assistop/device_discovery/deviceToggle.sh $device $toggle"

# If presented with a yes/no option it will input yes and then type in passed, otherwise type password
expect {
	"(yes/no)?"
	{ 
		send -- "yes\r"
		expect "assword:"
		send "raspberry\r";
	}
	"assword:"
	{
		send -- "raspberry\r";
	}
}

interact
