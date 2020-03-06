from Sockets.SocketServer import SocketServer
import RPi.GPIO as GPIO
import time

class Server(SocketServer):

    def __init__(self, ip, port):
        SocketServer.__init__(self, ip, port)

    # Implement socket code
    def listen_connection(self):
        self.open_connection()
        print("Connected client :", self.clientAddress)
        msg = ''
        while True:
            in_data = self.receive_package(1024)
            msg = in_data.decode()
            if msg == '1':
                print(msg,',')
                GPIO.output(18, GPIO.HIGH)
            if msg == '0':
                print(msg,',')
                GPIO.output(18, GPIO.LOW)
            if msg == 'bye':
                break
            #print("From Client :", msg)
            #out_data = input()
            #self.send_message(bytes(out_data, 'UTF-8'))

        #print("Client disconnected...")
        self.close_connection()

GPIO.setmode(GPIO.BCM)
serv = Server("192.168.0.139",10000)
GPIO.setup(18,GPIO.OUT)
serv.listen_connection()
GPIO.cleanup()
