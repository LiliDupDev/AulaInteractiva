from RFID_Listener import RFID_Listener
import Server
import threading

########################################################################################################################
import sys

ip = sys.argv[1]
port = sys.argv[2]

if __name__ == "__main__":
    port_number=int(port)
    rfid = RFID_Listener(ip, port)
    light = Server(ip,port)

    thread_light = threading.Thread(target=light.listen_connection, args=())
    thread_rfid = threading.Thread(target=rfid.start, args=())

    #start threads
    thread_light.start()
    thread_rfid.start()




