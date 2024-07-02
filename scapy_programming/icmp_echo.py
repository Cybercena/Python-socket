from scapy.all import *
import ipaddress

def icmp_ping(ip):
    icmp = ICMP()
    ip_packet = IP(dst=ip)
    request = ip_packet / icmp
    reply = sr1(request, timeout=2, verbose=False)

    if reply:
        print(f"Host {ip} is live")
       
       


def single_ip():
    try:
        ip = input("Enter single IP address to ping: ")
        icmp_ping(ip)
    except KeyboardInterrupt:
        print("\nPing process interrupted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def multiple_ips():
    try:
        ips = input("Enter multiple IP addresses separated by comma: ").split(',')
        for ip in ips:
            ip = ip.strip()
            icmp_ping(ip)
    except KeyboardInterrupt:
        print("\nPing process interrupted.")
        return
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def ip_range():
    try:
        start = input("Enter starting IP address of range: ")
        end = input("Enter ending IP address of range: ")
        
        ip_range = [str(ip) for ip in ipaddress.IPv4Network(f"{start}/{end}", strict=False).hosts()]
        for ip in ip_range:
            icmp_ping(ip)
    except KeyboardInterrupt:
        print("\nPing process interrupted.")
        return
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def subnet():
    try:
        subnet = input("Enter subnet in CIDR notation (e.g., 192.168.1.0/24): ")
        ips = [str(ip) for ip in ipaddress.IPv4Network(subnet).hosts()]
        for ip in ips:
            icmp_ping(ip)
    except KeyboardInterrupt:
        print("\nPing process interrupted.")
        return
    except Exception as e:
        print(f"An error occurred: {str(e)}")


#printing the Intro banner
def Banner():
    art = """
 .-----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____  _____  | || |  _________   | || |  _________   | || |  _______     | || |      __      | |
| ||_   \|_   _| | || | |_   ___  |  | || | |  _   _  |  | || | |_   __ \    | || |     /  \     | |
| |  |   \ | |   | || |   | |_  \_|  | || | |_/ | | \_|  | || |   | |__) |   | || |    / /\ \    | |
| |  | |\ \| |   | || |   |  _|  _   | || |     | |      | || |   |  __ /    | || |   / ____ \   | |
| | _| |_\   |_  | || |  _| |___/ |  | || |    _| |_     | || |  _| |  \ \_  | || | _/ /    \ \_ | |
| ||_____|\____| | || | |_________|  | || |   |_____|    | || | |____| |___| | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 __________________________________________________________________________________________________
    """
    print(art)
Banner()
if __name__ == "__main__":
    try:
        while True:
            print("\nMenu:")
            print("1. Ping a single IP")
            print("2. Ping multiple IPs")
            print("3. Ping IP range")
            print("4. Ping subnet")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                single_ip()
            elif choice == '2':
                multiple_ips()
            elif choice == '3':
                ip_range()
            elif choice == '4':
                subnet()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    except KeyboardInterrupt:
        print("\nExiting program due to keyboard interrupt.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
