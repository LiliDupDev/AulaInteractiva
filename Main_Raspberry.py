import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import threading
from Observer import Observer
from RFIDMonitor import RFIDMonitor
from Server_Rasp import Server



# Start the monitor for photoresistant
def process_observer(ip, port):
    try:
        obs = Observer(ip, port)
        GPIO.setmode(GPIO.BCM)
        obs.run()
    except:
        raise
    finally:
        GPIO.cleanup()

# Turn on/off the ligth
def process_light(ip, port):
    try:
        GPIO.setmode(GPIO.BCM)
        serv = Server(ip, port)
        GPIO.setup(18,GPIO.OUT)
        serv.listen_connection()
    except:
        raise
    finally:
        GPIO.cleanup()

def process_RFID(ip, port):
    rfid = RFIDMonitor(ip, port)
    rfid.start_monitor()

########################################################################################################################
import sys

ip = sys.argv[1]
port = sys.argv[2]

if __name__ == "__main__":
    port_number=int(port)
    thread_observer = threading.Thread(target=process_observer, args=(ip, port_number))
    thread_light = threading.Thread(target=process_light, args=(ip, port_number))
    thread_rfid = threading.Thread(target=process_RFID, args=(ip, port_number))

    #start threads
    thread_observer.start()
    thread_light.start()
    thread_rfid.start()