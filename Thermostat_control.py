import Pyro4
import serial

# ns = Pyro4.locateNS()
# uri=ns.lookup('thermostat')
# server = Pyro4.Proxy(uri)

server = Pyro4.Proxy("PYRO:thermostater.server@192.168.100.150:50000")
if __name__ == '__main__':
    try:
        arduino = serial.Serial('COM3', baudrate=9600, timeout=1.0)
        while True:
            temperatura = (arduino.readline()).decode()
            #print(temperatura)
            print(server.evaluateTemperature(26))
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit


