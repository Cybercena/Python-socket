#client in udp socket
import socket

def run_udp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_ip = "127.0.0.1"
    port = 8000
    while True:
        msg = input("Enter message:")
        client.sendto(msg.encode("utf-8"),(server_ip,port))
        response , _ = client.recvfrom(1024)
        response = response.decode("utf-8")

        if response.lower() == "closed":
            break
        # print(f"Received:{response}")
    client.close()
run_udp_client()