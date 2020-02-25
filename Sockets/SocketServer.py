import socket

LOCALHOST = "127.0.0.1"
PORT = 1800
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to address
server.bind((LOCALHOST, PORT))

#Enable the server to accept connections, it specifies the number of
#unaccepted connections that the system will allow before refusing
# new connections.
server.listen(1)

print("Server started")
print("Waiting for client request..")
clientConnection, clientAddress = server.accept()
print("Connected clinet :", clientAddress)
msg = ''
while True:
    #Receive data from the socket. The return value is a bytes object
    #representing the data received. The maximum amount of data to be
    #received at once is specified by bufsize.
    in_data = clientConnection.recv(1024)
    msg = in_data.decode()
    if msg == 'bye':
        break
    print("From Client :", msg)
    out_data = input()
    clientConnection.send(bytes(out_data, 'UTF-8'))
print("Client disconnected....")

#Mark the socket closed.
clientConnection.close()