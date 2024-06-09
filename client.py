#importing the library
import socket
# creating function to run client 
def run_client():
    # creating instant of object socket 
    #first argument is address family of ip and second argument is type of socket we are going to use. here we use TCP client
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    server_port = 8000
    #establishing connection with server
    client.connect((server_ip,server_port))
    #communication loop for sending mesasge
    while True:
        msg = input("Enter message:")
        #encoding message from string to bit 
        client.send(msg.encode("utf-8")[:1024])

        response = client.recv(1024)
        #decoding message from byte to string
        response = response.decode("utf-8")
        # condition to close the connection 
        if response.lower() == "closed":
            break
        print(f"Reveived:{response}")
        #closing the connection 
    client.close()
    print("connection to server closed")
    #function calling
run_client()