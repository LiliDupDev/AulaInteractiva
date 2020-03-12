from RFID_Listener import RFID_Listener
from Server import Server
from subprocess import Popen
# import threading

########################################################################################################################
import sys

# ip = "192.168.0.144"#sys.argv[1]
# port = "8000"#sys.argv[2]
# port_2 = 9000
#
# if __name__ == "__main__":
#     port_number=int(port)
#     rfid = RFID_Listener(ip, port_number)
#     light = Server(ip, port_2)

Popen(["python3", "C:\\Users\\Lili\\Documents\\GitHub\\AulaInteractiva\\RFID_Listener.py"])
Popen(["python3", "C:\\Users\\Lili\\Documents\\GitHub\\AulaInteractiva\\Server.py"])
#Popen(["python3", "/home/johngr/psdirc/TestBot3.py"])

    # #rfid.start()
    # thread_light = threading.Thread(target=light.listen_connection, args=())
    # thread_rfid = threading.Thread(target=rfid.start, args=())
    #
    # #start threads
    # thread_light.start()
    # thread_rfid.start()




