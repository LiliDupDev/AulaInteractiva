from RPC.ClientRPC import clientRPC
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from datetime import datetime

class RFIDMonitor(clientRPC):

    def __init__(self, ip, port):
        clientRPC.__init__(self, ip, port)

    def start_monitor(self):
        reader = SimpleMFRC522()
        try:
            while (True):
                id, name = reader.read()
                now = datetime.now()
                # now.year.month.day
                self.Proxy.save_data(id, name, now)
                # print(id)
                # print(text)
                # print("Fecha: ", now)
        except:
            raise
        finally:
            GPIO.cleanup()
    