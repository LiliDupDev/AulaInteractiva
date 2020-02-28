from Sockets.SocketServer import SocketServer
import Observer

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
            #print(msg)
            try:
                value = int(msg)
                if value > 10000:
                    obs = Observer("192.168.0.139", "10000")
                    obs.run2('0')
            except:
                print(msg)
            #self.send_message(bytes(str(value), 'UTF-8'))

            #print("From Client :", msg)
            #out_data = input()
            #self.send_message(bytes(out_data, 'UTF-8'))
        #print("Client disconnected...")
        self.close_connection()


serv = Server("192.168.0.145", 8080)
serv.listen_connection()
