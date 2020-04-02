import pika
# This script must be executed on server machine


# Stablish connection with server
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')) # IP doesn't change is localhost

channel = connection.channel()

# Declaring queue
channel.queue_declare(queue='rpc_queue')


def metal_detected(aula):
    detected="Metal has been detected at "+str(aula)
    connection_temp = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) # IP doesn't change is localhost
    channel_temp = connection_temp.channel()

    channel_temp.queue_declare(queue='Metal_Detected')

    channel.basic_publish(exchange='', routing_key='Metal_Detected', body=detected)
    print(detected)
    connection.close()
    return 1

def on_request(ch, method, props, body):
    n = int(body)

    #print(" [.] fib(%s)" % n)
    response = metal_detected(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)



print(" [x] Awaiting RPC requests")
channel.start_consuming()