import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))    # Raspberry IP
channel = connection.channel()

channel.queue_declare(queue='Metal_Detected')


def callback(ch, method, properties, body):
    print(" [x] Metal detectado en aula: %r" % body)
    # TODO: aqui se dispara el buzer


channel.basic_consume(
    queue='Metal_Detected', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()