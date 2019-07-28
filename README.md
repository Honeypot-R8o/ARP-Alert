# ARP-Alert
Software send an Email when a new Device is connected to your Network. For Raspberry Pi<br>
<br>
Installation on Rasperry Pi:<br>
<br>
copy the arp-alert.py to /home/pi/<br>
<br>
sudo pip3 install scapy<br>
sudo apt-get install tcpdump<br>
sudo apt-get install gedit<br>
sudo gedit /etc/rc.local<br>
-><br>
add line before exit 0:  sudo python3 /home/pi/arp-alert.py &<br>
<br>
gedit arp-alert.py<br>
edit line 13 with your Email-Account<br>
edit line 35 with your MAC-Address white list<br>
sudo reboot<br>
