from RPC.ServerRPC import ServerRPC

class RFID_Listener(ServerRPC):

    def __init__(self,ip,port):
        ServerRPC.__init__(self, ip, port)

    def start(self):
        self.connect_listen()

    # def save_data(self, id, name, date):
    #     f = open('myfile.txt', 'a')
    #     f.write('Identificador: ' +''+ id + ' Nombre: ' +'' + name + ' Fecha: ' +'' + date +'\n' )
    #     f.close()

#

if __name__ == "__main__":
    rfid = RFID_Listener("192.168.43.116", 3500)
    rfid.start()
    #rfid = RFID_Listener("192.168.0.144", 3500)

