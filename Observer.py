from Sockets.SocketClient import SocketClient
#import RPi.GPIO as GPIO
import time



class Observer(SocketClient):
    """mpin = 17
    tpin = 27
    cap = 0.000001
    adj = 2.130620985
    i = 0
    t = 0

    def LDR(self):
        try:
            lecture=0 
            GPIO.setup(self.mpin,GPIO.OUT)
            GPIO.setup(self.tpin,GPIO.OUT)
            GPIO.output(self.mpin,False)
            GPIO.output(self.tpin,False)
            time.sleep(0.2)
            GPIO.setup(self.mpin,GPIO.IN)
            time.sleep(0.2)
            GPIO.output(self.tpin,True)
            starttime = time.time()
            endtime = time.time()
            while (GPIO.input(self.mpin) == GPIO.LOW):
                endtime = time.time()
            measureresistance = endtime - starttime
            res = (measureresistance/self.cap)*self.adj
            self.i = self.i+1
            self.t = self.t + res
            if self.i == 10:
                lecture = self.t/self.i
                self.t = 0
                self.i = 0         
            return lecture
        except:
            GPIO.cleanup()
        """
    def __init__(self,ip,port):
        SocketClient.__init__(self,ip,port)

    def run2(self,message):
        self.open_connection()
        self.send_message(bytes(message, 'UTF-8'))
        self.close_connection()



    def run(self):
        self.open_connection()
        self.send_message(bytes("This is from Client", 'UTF-8'))
        #GPIO.setmode(GPIO.BCM)		

        
        while(True):
            #in_data = self.receive_package(1024)
            #print("From Server :", in_data.decode())
            out_data = "1"#str(self.LDR())
            print("Data", out_data)
            if out_data!='0':
                self.send_message(bytes(out_data, 'UTF-8'))
            if out_data == 'bye':
                break
        self.close_connection()
        
            

obs=Observer("192.168.0.139",10000)
#obs = Observer("192.168.0.139", 8080)
#GPIO.setmode(GPIO.BCM)
obs.run2("LILI CHAN")
#GPIO.cleanup()
		
