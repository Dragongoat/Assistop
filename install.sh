# Assistop install script

echo "Initializing Assistop installation..."

# Install dependencies for install
sudo apt update -y -qq
sudo apt upgrade -y -qq
sudo apt install -y -qq curl wget avahi-daemon raspberrypi-kernel raspberrypi-kernel-headers python3-pip nmap

# Link to install RaspAP: https://howtoraspberrypi.com/create-a-wi-fi-hotspot-in-less-than-10-minutes-with-pi-raspberry/
# Free up the wireless interface
echo 'Freeing up wireless interface. Previous configuration saved at /etc/wpa_supplicant.conf.sav'
sudo cp /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.sav
sudo cp ./templates/wpa_supplicant.conf.template /etc/wpa_supplicant/wpa_supplicant.conf

# Install hostapd and RaspAP using quick installer
echo 'Installing hostapd and RaspAP'
wget -q https://git.io/voEUQ -O /tmp/raspap && bash /tmp/raspap -y -o 0

echo 'Configuring network interfaces to static'
# Set static IP for eth0 and wlan0

#Get the dhcp info and set it as static
staticip=`ip addr show eth0 | grep -Po "inet \d+\.\d+\.\d+\.\d+" | sed "s/inet //"`
gateway=`ip route | grep default | grep -Po -m 1 "\d+\.\d+\.\d+\.\d+" | head -1`
network=`echo $staticip | sed "s/\([0-9]\+\.[0-9]\+\.[0-9]\+\.\)[0-9]\+/\10/"`

# Set static IP for eth0 and wlan0
while read line
do
        echo $line | sed "s/192.168.1.1/$gateway/g" | sed "s/192.168.1.0/$network/g" | sed "s/192.168.1.99/$staticip/g"
done < ./templates/interfaces.template > /etc/network/interfaces

# Let rapAP know about eth0
while read line
do
        echo $line | sed "s/192.168.1.1/$gateway/g" | sed "s/192.168.1.99/$staticip/g"
done < ./templates/eth0.ini.template > /etc/raspap/networking/eth0.ini

# Let rapAP know about wlan0
while read line
do
        echo $line | sed "s/192.168.1.1/$gateway/g" 
done < ./templates/wlan0.ini.template > /etc/raspap/networking/wlan0.ini
echo 'Renaming device'

# Set hostname to assistop
sudo sed -i 's/127\.0\.1\.1[[:blank:]]*raspberrypi/127.0.1.1\tassistop/1' /etc/hosts
sudo cp ./templates/hostname.template /etc/hostname

# Rename hotspot network
sudo sed -i 's/ssid=raspi-webgui/ssid=Assistop/g' /etc/hostapd/hostapd.conf

sudo rfkill unblock wifi; sudo rfkill unblock all

sed -i "s/^\(server\.port *= *\)[0-9]*/\18080/g" /etc/lighttpd/lighttpd.conf

# Link to install Docker: https://linuxhint.com/install_docker_on_raspbian_os/

# Use Docker quick install script
curl -sSL https://get.docker.com | sh

# Add user pi to docker group
sudo usermod -aG docker pi

# Link to install Docker-compose: https://stackoverflow.com/questions/58747879/docker-compose-usr-local-bin-docker-compose-line-1-not-command-not-found

# Install latest version of docker-compose via pip3
yes | sudo pip3 install docker-compose

# Add a cron job to run check_devices.py
(crontab -l -u pi; echo "* * * * * /home/pi/Assistop/device_discovery/check_devices.py") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -u pi -
(crontab -l -u pi; echo "* * * * * (sleep 30 ; /home/pi/Assistop/device_discovery/check_devices.py)") 2>&1 | grep -v "no crontab" | sort | uniq | crontab -u pi -

echo 'Installation complete. A reboot is required to finish installation.'
while true
do
	read -p 'Reboot now? (Y/N): ' answer
	case $answer in 
		[yY]* ) sudo reboot now
			break;;

		[nN]* ) exit;;

		* )     echo "Error, please enter Y or N.";;
	esac
done
