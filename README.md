# ARP-Alert
Software Send an Email-Alert if a new Device connect to your Network. For Raspberry Pi

Installation on Rasperry Pi:

copy the arp-alert.py to /home/pi/

sudo pip3 install scapy
sudo apt-get install tcpdump
sudo apt-get install gedit
sudo gedit /etc/rc.local
->
add line before exit 0:  sudo python3 /home/pi/arp-alert.py &

sudo reboot
