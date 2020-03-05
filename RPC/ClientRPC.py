import xmlrpc.client
# from datetime import datetime

class clientRPC(object):
    IP = None
    PORT = 9000
    Proxy = None

    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
        self.Proxy = xmlrpc.client.ServerProxy('http://'+ self.IP+':'+self.PORT,allow_none=True)

    # def save_data(self, data):
    #     date = str(datetime.now())
    #     self.Proxy.save_data("2", "COnstantinho", date)



# if __name__ == '__main__':
#     cl = clientRPC("localhost", "9000")
#     cl.save_data('127.0.0.1','9000')


