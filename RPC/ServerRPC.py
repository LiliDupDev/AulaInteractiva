from xmlrpc.server import SimpleXMLRPCServer

class ServerRPC(object):
    IP = None
    PORT = 9000
    server = None

    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port

    def connect_listen(self):
        self.server = SimpleXMLRPCServer((self.IP, self.PORT), logRequests=True, allow_none=True)
        self.server.register_instance(ServerRPC(self.IP, self.PORT))
        try:
            print("Server running ...")
            #print("Use control-c to exit")
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("Exiting")

    def save_data(self, id, name, datee):
    #     # print("Identificador:",id)
    #     # print("Nombre:", name)
    #     # print("Fecha:", datee)
         f = open('myfile.txt', 'a')
         f.write('Identificador: ' +''+ id + ' Nombre: ' +'' + name + ' Fecha: ' +'' + datee +'\n' )
         f.close()



# if __name__ == '__main__':
#     ser = ServerRPC("127.0.0.1", 9000)
#     ser.connect_listen()