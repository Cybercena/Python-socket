import socket

def run_Udpserver():
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_ip = "127.0.0.1"
    port = 8000

    server.bind((server_ip,port))
    print(f"Listening on {server_ip}:{port}")

    while True:
        data , client_address = server.recvfrom(1024)
        data = data.decode("utf-8")

        if data.lower()=="close":
            server.sendto("Closed".encode("utf-8"),client_address)
            break

        print(f"Received from :{data}")
        response = "accepted".encode("utf-8")
        server.sendto(response,client_address)
    server.close()
run_Udpserver()