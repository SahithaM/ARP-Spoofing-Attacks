# ARP-Spoofing-Attacks
This is Advanced Computer Network Assignment that I have done during my course work

This repository contains implementations of various ARP spoofing attacks demonstrating ARP cache poisoning.

## Task 1: ARP Cache Poisoning
### Task 1A: Spoofed ARP Request(`task1A.py`)
```
sudo python3 scripts/task1A.py
```
- Created fake ARP request with attacker's MAC as Victim B's IP
- Result: Host A's ARP cache poisoned with attacker's MAC
- *[Image: media/image1.png]*

### Task 1B: Spoofed ARP Reply(`task1B.py`)
```
sudo python3 scripts/task1B.py
```
- Cleared ARP cache before attack
- Created fake ARP reply with attacker's MAC
- Challenge: Host A rejects unsolicited replies (stateful behavior)
- Solution: Create incomplete entry first via `ping`
- *[Image: media/image2.png]*

### Task 1C: Spoofed Gratuitous ARP(`task1C.py`)
```
sudo python3 scripts/task1C.py
```
- Sent broadcast message with identical source/destination IP
- Requires existing incomplete entry in ARP cache
- Affects only hosts with pending ARP requests
- *[Image: media/image3.png]*

## Task 2: MITM Attack on Telnet(`task2.py`)
```
sudo python3 scripts/task2.py
```
- Poisoned both Host A and Host B ARP caches
- Intercepted and forwarded Telnet traffic
- *[Image: media/image4.png]*

## Task 3: MITM Attack on Netcat(`task3.py`)
```
sudo python3 scripts/task3.py
```
- Similar ARP poisoning technique
- Manipulated TCP payload during interception
- *[Image: media/image5.png]*
