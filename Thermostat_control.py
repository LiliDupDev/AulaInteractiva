import Pyro4
import serial

#This script monitor the temperature sensor and call the remote object Thermostater to evaluate temperature
# ns = Pyro4.locateNS()
# uri=ns.lookup('thermostat')
# server = Pyro4.Proxy(uri)

# Server address
server = Pyro4.Proxy("PYRO:thermostater.server@192.168.100.150:50000")

if __name__ == '__main__':
    try:
        arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1.0)
        while True:
            temp = (arduino.readline()).decode()
            print(server.evaluateTemperature(temp))
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit


