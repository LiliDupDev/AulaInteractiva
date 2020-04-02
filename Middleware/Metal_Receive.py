import pika
import threading
# This script must be executed on server machine


# Stablish connection with server
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')) # IP doesn't change is localhost

channel = connection.channel()

# Declaring queue
channel.queue_declare(queue='rpc_queue')

# Declaring exchange
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


def send_security_message(message):
    routing_key="Metal.security"

    channel.basic_publish(
        exchange='topic_logs', routing_key=routing_key, body=message)
    #print(" [x] Sent %r:%r" % (routing_key, message))
    #connection.close()

# Process when a metal is detected
def metal_detected(aula):
    detected="Metal has been detected at Aula: "+str(aula)
    print(detected)
    send_security_message(detected)
    return 1

def on_request(ch, method, props, body):
    n = int(body)

    response = metal_detected(n)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=2)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)



print(" [x] Listening ... ")
channel.start_consuming()