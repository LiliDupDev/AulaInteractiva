from RMI import Server_RMI
from RMI import RMI_objects

#This class starts the RMI server, remember first run the command pyro4-ns -n 127.0.0.1 in your terminal

if __name__ == '__main__':
    try:
        thermostat = RMI_objects.Thermostat()           # Creating remote object
        ser = Server_RMI.Server_RMI()                   # Server class
        ser.register_object(thermostat,"thermostat")    # Registering remote object
        ser.start_server()                              # Start server
        # ser.evaluateTemperature()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
