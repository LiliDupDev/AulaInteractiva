from Sockets.SocketServer import SocketServer

class Server(SocketServer):

    def __init__(self, ip, port):
        SocketServer.__init__(self, ip, port)

    # Implement socket code
    def listen_connection(self):
        self.open_connection()
        print("Connected client :", self.clientAddress)
        msg = ''
        while True:
            in_data = self.receive_package(1024)
            msg = in_data.decode()
            print(msg)
            if msg == 'bye':
                break
            #print("From Client :", msg)
            #out_data = input()
            #self.send_message(bytes(out_data, 'UTF-8'))

        print("Client disconnected...")
        self.close_connection()


serv = Server("127.0.0.1", 8080)
serv.listen_connection()
