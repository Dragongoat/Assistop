# Assistop install script

# Install dependencies for install
sudo apt update -y -qq
sudo apt upgrade -y -qq
sudo apt install -y -qq curl wget

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
sudo cp ./templates/interfaces.template /etc/network/interfaces

# Let raspAP know about eth0 config
sudo cp ./templates/eth0.ini.template /etc/raspap/networking/eth0.ini 

# Let raspAP know about wlan0 config
sudo cp ./templates/wlan0.ini.template /etc/raspap/networking/wlan0.ini

echo 'Renaming device'
# Make sure device can use hostname.local
sudo apt update -y -qq
sudo apt upgrade -y -qq
sudo apt install -y -qq avahi-daemon

# Set hostname to assistop
sudo sed -i 's/127\.0\.1\.1[[:blank:]]*raspberrypi/127.0.1.1\tassistop/1' /etc/hosts
sudo cp ./templates/hostname.template /etc/hostname

# Rename hotspot network
sudo sed -i 's/ssid=raspi-webgui/ssid=Assistop/g' /etc/hostapd/hostapd.conf

sudo rfkill unblock wifi; sudo rfkill unblock all

# Link to install Docker: https://linuxhint.com/install_docker_on_raspbian_os/

# Install necessary headers for docker to work
sudo apt install -y -qq raspberrypi-kernel raspberrypi-kernel-headers

# Use Docker quick install script
curl -sSL https://get.docker.com | sh

# Add user pi to docker group
sudo usermod -aG docker pi

# Link to install Docker-compose: https://stackoverflow.com/questions/58747879/docker-compose-usr-local-bin-docker-compose-line-1-not-command-not-found

# Install latest version of docker-compose via pip3
sudo apt install python3-pip
yes | sudo pip3 install docker-compose

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