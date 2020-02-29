from Sockets.SocketServer import SocketServer
from Sockets.SocketClient import SocketClient
import threading

class Server(SocketServer):
    def __init__(self, ip, port):
        SocketServer.__init__(self, ip, port)

    # Implement socket code
    def listen_connection(self):
        self.open_connection()
        print("Connected client :", self.clientAddress)
        client = SocketClient('192.168.0.139', 10000)
        client.open_connection()
        while True:
            in_data = self.receive_package(1024)
            msg = in_data.decode()
            print(msg)
            try:
                value = float(msg)
                if value > 10000:
                    thread1 = threading.Thread(target=self.send_message_as_client, args=(client, '1'))
                    thread1.start()
                    thread1.join()
                else:
                    thread1 = threading.Thread(target=self.send_message_as_client, args=(client, '0'))
                    thread1.start()
                    thread1.join()
            except:
                print(msg)
                break

        client.open_connection()
        self.close_connection()

    def send_message_as_client(self,socket,message):
        socket.send_message(bytes(message, 'UTF-8'))


serv = Server("192.168.0.144", 8080)
serv.listen_connection()
