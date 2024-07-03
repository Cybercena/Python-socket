#!/usr/bin/env python3
from scapy.all import *
import ipaddress

def icmp_ping(ip):
    icmp = ICMP()
    ip_packet = IP(dst=ip)
    request_icmp = ip_packet / icmp
    reply_icmp = sr1(request_icmp, timeout=2, verbose=False)

    if reply_icmp:
        print(f"Host {ip} is live (ICMP)")

def arp_request(ip):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    reply_arp, _ = srp(arp_request, timeout=2, verbose=False)

    if reply_arp:
        print(f"Host {ip} is live (ARP) - MAC: {reply_arp[0][1].src}")

def single_ip(scan_type):
    try:
        ip = input(f"Enter single IP address to {scan_type}: ").strip()

        if scan_type == 'icmp':
            icmp_ping(ip)
        elif scan_type == 'arp':
            arp_request(ip)
    except KeyboardInterrupt:
        print(f"\n{scan_type.capitalize()} scan process interrupted.")

def multiple_ips(scan_type):
    try:
        ips = input(f"Enter multiple IP addresses separated by comma to {scan_type}: ").split(',')

        for ip in ips:
            ip = ip.strip()
            if scan_type == 'icmp':
                icmp_ping(ip)
            elif scan_type == 'arp':
                arp_request(ip)
    except KeyboardInterrupt:
        print(f"\n{scan_type.capitalize()} scan process interrupted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def ip_range(scan_type):
    try:
        start = input(f"Enter starting IP address of range to {scan_type}: ").strip()
        end = input(f"Enter ending IP address of range to {scan_type}: ").strip()
        
        ip_range = [str(ip) for ip in ipaddress.IPv4Network(f"{start}/{end}", strict=False).hosts()]
        for ip in ip_range:
            if scan_type == 'icmp':
                icmp_ping(ip)
            elif scan_type == 'arp':
                arp_request(ip)
    except KeyboardInterrupt:
        print(f"\n{scan_type.capitalize()} scan process interrupted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def subnet(scan_type):
    try:
        subnet = input(f"Enter subnet in CIDR notation (e.g., 192.168.1.0/24) to {scan_type}: ").strip()
        
        ips = [str(ip) for ip in ipaddress.IPv4Network(subnet).hosts()]
        for ip in ips:
            if scan_type == 'icmp':
                icmp_ping(ip)
            elif scan_type == 'arp':
                arp_request(ip)
    except KeyboardInterrupt:
        print(f"\n{scan_type.capitalize()} scan process interrupted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def Banner():

    art = """
            _   _   ______   _______   _____             
            | \ | | |  ____| |__   __| |  __ \      /\    
            |  \| | | |__       | |    | |__) |    /  \   
            | . ` | |  __|      | |    |  _  /    / /\ \  
            | |\  | | |____     | |    | | \ \   / ____ \ 
            |_| \_| |______|    |_|    |_|  \_\ /_/    \_\ 
            ______________________________________________
                Network Scanning Tools By Cybercena
    """
    print(art)

if __name__ == "__main__":
    try:
        Banner()  # Print the banner
        while True:
            print("\nChoose scan type:")
            print("1. ICMP")
            print("2. ARP")
            print("3. Exit")
            scan_choice = input("Enter your choice (1-3): ")

            if scan_choice == '1':
                print("\nICMP Scan:")
                print("1. Scan a single IP")
                print("2. Scan multiple IPs")
                print("3. Scan IP range")
                print("4. Scan subnet")
                icmp_choice = input("Enter your choice (1-4): ")

                if icmp_choice == '1':
                    single_ip('icmp')
                elif icmp_choice == '2':
                    multiple_ips('icmp')
                elif icmp_choice == '3':
                    ip_range('icmp')
                elif icmp_choice == '4':
                    subnet('icmp')
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

            elif scan_choice == '2':
                print("\nARP Scan:")
                print("1. Scan a single IP")
                print("2. Scan multiple IPs")
                print("3. Scan IP range")
                print("4. Scan subnet")
                arp_choice = input("Enter your choice (1-4): ")

                if arp_choice == '1':
                    single_ip('arp')
                elif arp_choice == '2':
                    multiple_ips('arp')
                elif arp_choice == '3':
                    ip_range('arp')
                elif arp_choice == '4':
                    subnet('arp')
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

            elif scan_choice == '3':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    except KeyboardInterrupt:
        print("\nExiting program due to keyboard interrupt.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
