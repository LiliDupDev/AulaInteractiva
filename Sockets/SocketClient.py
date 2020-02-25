import socket

SERVER = "127.0.0.1"
PORT = 1800

# Building socket( Address Format Internet, )
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to a remote socket at address.
client.connect((SERVER, PORT))

#Send data to the socket. The socket must be connected to a remote socket.
#this method continues to send data from bytes until either all data has been sent
#or an error occurs
client.sendall(bytes("This is from Client", 'UTF-8'))

while True:
    # Receive data from the socket. The return value is a bytes object
    # representing the data received. The maximum amount of data to be
    # received at once is specified by bufsize.
    in_data = client.recv(1024)
    print("From Server :", in_data.decode())
    out_data = input()
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'bye':
        break
client.close()