#coding=utf8
from scapy.all import *
for i in range(2,255):
    ip=IP(src='192.168.10.%d'%i,dst='192.168.10.194') 
    tcp=TCP(sport=1024)
    http="GET / HTTP/1.0\r\n"
    print sr1(ip/tcp/http)
