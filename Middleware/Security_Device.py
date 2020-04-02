import pika
from datetime import datetime

credentials = pika.PlainCredentials('client', 'cl-123')
parameters = pika.ConnectionParameters("192.168.56.1", 5672, '/', credentials)  # server IP and port
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_key = "*.security" #sys.argv[1:] # All messages related with security

channel.queue_bind(
    exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting. To exit press CTRL+C')


def callback(ch, method, properties, body):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print( " [x] %r ---> %r:%r" % (dt_string, method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()