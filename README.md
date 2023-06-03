# n3tscan
Faast ping sweep of a /24 network written in Python

Multi-threaded. Sends all the pings at once. </br>Expect complete results instantly (within 1/4th of a second to be approximate).

Disclaimer: It will only show IPs that respond to an ICMP echo request aka ping.. so mostly Linux machines.



Installation:
1. Download n3tscan.py
2. Run using python

Usage example: 

`$ python n3tscan.py 192.168.0`

If you use it regularly to scan your LAN, add it as an alias in Linux 
For eg. if your n/w is 192.168.1.0/24, add this to your .bashrc or .zhrc

`alias netscan='python /path/to/n3tscan.py 192.168.1'`

Then simply type:

`netscan`

when you want to instantly know IPs in your LAN.
