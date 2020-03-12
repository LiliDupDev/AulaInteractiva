import Pyro4

ns = Pyro4.locateNS()
uri=ns.lookup('thermostat')
server = Pyro4.Proxy(uri)

if __name__ == '__main__':
    try:
        print(server.evaluateTemperature(26))
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit


