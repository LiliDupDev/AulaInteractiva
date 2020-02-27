from Sockets.SocketClient import SocketClient

class Observer(SocketClient):

    def __init__(self,ip,port):
        SocketClient.__init__(self,ip,port)

    def run(self):
        self.open_connection()
        self.send_message(bytes("This is from Client", 'UTF-8'))

        while(True):
            in_data = self.receive_package(1024)
            print("From Server :", in_data.decode())
            out_data = input()
            self.send_message(bytes(out_data, 'UTF-8'))
            if out_data == 'bye':
                break
        self.close_connection()


obs = Observer("127.0.0.1", 8080)
obs.run()
