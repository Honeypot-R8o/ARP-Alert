#! /usr/bin/env python3

from scapy.all import ARP, sniff
import smtplib
import requests

def arp_display(pkt):
	if (pkt[ARP].op == 1) or (pkt[ARP].op == 2):
		if str(pkt[ARP].hwsrc) not in macWhiteList:
			print("Alert, new Device found. MAC: " + pkt[ARP].hwsrc)
			vendor = requests.get('http://api.macvendors.com/' + str(pkt[ARP].hwsrc)[:-5]+'00:00').text
			print(vendor)
			send_email('ms1smtp.webland.ch',465,'device@yourEmail.com','yourPassowrd','to@email1234.com','Private-Network-Alert','MAC-Alert: ' + str(pkt[ARP].hwsrc) + " Vendor: " + vendor)
			macWhiteList.append(str(pkt[ARP].hwsrc))			

def send_email(mail_domain, mail_port, mail_user, mail_password, mail_recipient, subject, body):
	FROM = mail_user
	TO = mail_recipient
	SUBJECT = subject
	TEXT = body
	message = "From: "+FROM + "\nTo: " + TO + "\nSubject: " + SUBJECT + "\n\n" + TEXT + "\n\n"
	try:
		server = smtplib.SMTP_SSL(mail_domain, mail_port)
		server.ehlo()
		#server.starttls()
		server.login(mail_user, mail_password)
		server.sendmail(FROM, TO, message)
		server.close()
		return 'successfully sent the mail'
	except Exception as e:
		return "failed to send mail"
 


macWhiteList=["00:11:32:61:12:34","00:25:36:d6:12:34"] # use lowercase characters

sniff(prn=arp_display, filter="arp", iface="eth0", store=0)

