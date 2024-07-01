from scapy.all import *

def icmp_ping(ip):
    icmp = ICMP()
    ip_packet = IP(dst=ip)
    request = ip_packet / icmp
    reply = sr1(request, timeout=2, verbose=False)
    
    if reply:
        print(f"Host {ip} is live")
    else:
        print(f"Host {ip} is unreachable")

# Example usage: Replace '192.168.1.1' with the IP address you want to ping
icmp_ping('192.168.18.11')
