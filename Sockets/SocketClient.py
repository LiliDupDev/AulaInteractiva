import socket

class SocketClient():
    IP = None       # Server IP
    PORT = 1800     # Default PORT to stablish connection
    client = None   # Client socket

    def __init__(self, ip, port):
        self.IP=ip
        self.PORT=port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open_connection(self):
        self.client.connect((self.IP, self.PORT))

    def close_connection(self):
        self.client.close()

    def send_message(self, bytes_message):
        self.client.sendall(bytes_message)

    def receive_package(self,size):
        return self.client.recv(size)