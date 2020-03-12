import Pyro4

@Pyro4.expose
class Server_RMI:

    @property
    def daemon(self):
        return self._daemon

    @daemon.setter
    def daemon(self, value):
        self._daemon = value

    @property
    def ns(self):
        return self.ns

    @daemon.setter
    def ns(self, value):
        self._ns = value


    def __init__(self):
        self._daemon = Pyro4.Daemon()
        self._ns = Pyro4.locateNS()

    def register_object(self, object, name):
        uri = self._daemon.register(object)
        self._ns.register(name, str(uri))

    def start_server(self):
        # self.daemon = Pyro4.Daemon()
        # self.ns = Pyro4.locateNS()
        # self.uri = daemon.register(object)
        #ns.register('ANDIK.server', str(uri))
        print(f'Ready to listen')
        #print(uri)
        self._daemon.requestLoop()


