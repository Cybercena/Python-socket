#creating tcp port scanner using tcp socket.
import socket

def port_scan(target_host, target_port):
    #creating a tcp socket
    scanner_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #set a timeout for the connection attempt
    scanner_socket.settimeout(1)
    #attempt for connecting to target port
    result = scanner_socket.connect_ex((target_host, target_port)) #we use exception while connecting , if connection established connect_ex() returns 0
    #check if connection was successfull
    if result == 0:
        print(f"port{target_port} is open")
    else:
        print(f"port{target_port} is closed")
    # close the socket 
    scanner_socket.close()

def main():
    target_host = input("Enter the target host IP address:")
    start_port = int(input("Enter the starting port number:"))
    end_port = int(input("Enter the ending port number:"))

    #performing port scanning
    print(f"Scanning ports {start_port} to {end_port} on host {target_host}")
    for port in range(start_port, end_port + 1):
        port_scan(target_host,port)
main()
