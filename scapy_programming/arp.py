from scapy.all import *
import ipaddress

def arp_request(ip):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    reply_arp, _ = srp(arp_request, timeout=2 , verbose=False)

    if reply_arp:
        print(f"Host {ip} is live - MAC:{reply_arp[0][1].hwsrc}")
       

ip = input("Enter the ip:")
arp_request(ip)
