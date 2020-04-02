import pika
import uuid

#This script must be executed in Rasp
class Metal_Detector(object):
    def __init__(self):
        credentials = pika.PlainCredentials('client','cl-123')
        parameters = pika.ConnectionParameters("192.168.56.1",5672,'/',credentials) # server IP and port
        self.connection = pika.BlockingConnection(parameters)

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


#fibonacci_rpc = FibonacciRpcClient()
metal_client = Metal_Detector()
# TODO: Aqui va el codigo que monitorea el sensor de metal
print(" Metal detected ")           # Cuando se detecta el metal debe ejecutar este codigo
response = metal_client.call(5)     # El parametro es supuestamente el aula en que detecto el arma
print(" [.] Got %r" % response)
# la variable response regresa un 1 para que se encienda el buzzer
