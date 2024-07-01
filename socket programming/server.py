#importing library hai !
import socket
# creating run_server function to run server 
def run_server():
    # creating socket object with first parameter adress family and second parameter types of socket 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1" # sever running on local host 
    port = 8000
    #biniding the socket to specific addreass and ports:
    server.bind((server_ip,port)) #we need single parameter so we are using tuple with two values
    # now its time for listening for incoming connection 
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    #accepting incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connectin from {client_address[0]}:{client_address[1]}")

    #creating communication loop:
    #receive data from the client:
    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8")

        if request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break
        print(f"Received:{request}")
    
    #sending response back to client
        response = "accepted".encode("utf-8")
        client_socket.send(response)

    #close connection socket with the client
    client_socket.close()
    print("Connection to client closed")
    server.close()
run_server()
