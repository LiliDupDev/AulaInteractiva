from RPC.ServerRPC import ServerRPC

class RFID_Listener(ServerRPC):

    def __init__(self,ip,port):
        ServerRPC.__init__(ip, port)

    def start(self):
        self.connect_listen()

    def save_data(self, id, name, date):
        f = open('myfile.txt', 'a')
        f.write('Identificador: ' +''+ id + ' Nombre: ' +'' + name + ' Fecha: ' +'' + date +'\n' )
        f.close()
