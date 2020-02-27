import socket

class SocketServer(object):
    IP = None                       # Server IP
    PORT = 1800                     # Default PORT to stablish connection
    IS_CLIENT_CONNECTED = False     # Flag that indicates if a client is connected
    server = None                   # Server socket
    clientConnection = None         # Client connected
    clientAddress = None            # Client IP

    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IS_CLIENT_CONNECTED=False

    # Create connection and start listening, change the flag IS_CLIENT_CONNECTED
    def open_connection(self):
        self.server.bind((self.IP, self.PORT))
        self.server.listen(1)
        self.clientConnection, self.clientAddress = self.server.accept()
        self.IS_CLIENT_CONNECTED = True


    # Close client connection
    def close_connection(self):
        self.clientConnection.close()

    def receive_package(self,size):
        return self.clientConnection.recv(size)

    def send_message(self, bytes_message):
        self.clientConnection.sendall(bytes_message)