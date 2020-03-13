import Pyro4

@Pyro4.expose
class Thermostater(object):

    def evaluateTemperature(self,temperature):
        if temperature < 20:
            a = 'La temperatura esta baja, lo recomendado es entre 20°C y 25°C'
            return a
        if temperature > 25:
            a = 'La temperatura esta alta, lo recomendado es entre 20°C y 25°C'
            return a
        elif temperature >= 20 & temperature <= 25:
            a = 'Esta bien k'
            return a

    def start_server(self):
        daemon = Pyro4.Daemon()
        ns = Pyro4.locateNS()
        uri = daemon.register(Thermostater)
        ns.register('thermostater.server', str(uri))
        print(f'Ready to listen')
        print(uri)
        daemon.requestLoop()



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

