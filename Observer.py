from Sockets.SocketClient import SocketClient
import RPi.GPIO as GPIO
import time

mpin = 17
tpin = 27
GPIO.setmode(GPIO.BCM)
cap = 0.000001
adj = 2.130620985
i = 0
t = 0

def LDR():
    i = 0
    t = 0
    GPIO.setup(mpin,GPIO.OUT)
	GPIO.setup(tpin,GPIO.OUT)
	GPIO.output(mpin,False)
	GPIO.output(tpin,False)
	time.sleep(0.2)
	GPIO.setup(mpin,GPIO.IN)
	time.sleep(0.2)
	GPIO.output(tpin,True)
	starttime = time.time()
	endtime = time.time()
	while (GPIO.input(mpin) == GPIO.LOW):
		endtime = time.time()
	measureresistance = endtime - starttime
	res = (measureresistance/cap)*adj
	i = i+1
	t= t + res
	if i == 10:
		t = t/i
		return(t)
		

class Observer(SocketClient):

    def __init__(self,ip,port):
        SocketClient.__init__(self,ip,port)

    def run(self):
        self.open_connection()
        self.send_message(bytes("This is from Client", 'UTF-8'))

        while(True):
            in_data = self.receive_package(1024)
            print("From Server :", in_data.decode())
            out_data = LDR()
            self.send_message(bytes(str(out_data), 'UTF-8'))
            if out_data == 'bye':
                break
        self.close_connection()


obs = Observer("192.168.0.144", 8080)
obs.run()
