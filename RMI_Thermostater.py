import Pyro4

# Remote object
@Pyro4.expose
class Thermostater(object):

    #Based on the argument sent it calculates the right temperature
    # TODO: return must be compatible with an air conditioner
    def evaluateTemperature(self,temperature):
        if temperature < 20:
            a = 'La temperatura esta baja, lo recomendado es entre 20°C y 25°C'
            return a
        if temperature > 25:
            a = 'La temperatura esta alta, lo recomendado es entre 20°C y 25°C'
            return a
        elif temperature >= 20 & temperature <= 25:
            a = 'Esta bien'
            return a

    # Start the background process that will have the remote object
    def start_server(self):
        daemon = Pyro4.Daemon()
        ns = Pyro4.locateNS()                       # Locate name server
        uri = daemon.register(Thermostater)         # Create the identifier for the remote object
        ns.register('thermostater.server', str(uri))# Assing a name for the remote object
        print(f'Ready to listen')
        print(uri)
        daemon.requestLoop()                        # Leave the daemon running


# Connection string, this is the server connection and the port
Pyro4.Daemon.serveSimple({Thermostater: 'thermostater.server', }, host="192.168.0.144", port=50000, ns=False,
                            verbose=True)
if __name__ == '__main__':
    try:
        ser = Thermostater()
        ser.start_server()
        ser.evaluateTemperature()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit

