import pika
import logging
logging.basicConfig()
logging.getLogger('pika').setLevel(logging.DEBUG)

print "1"
credentials = pika.PlainCredentials('guest', 'guest')
print "2"
#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',15672, '/', credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))
print "3"
channel = connection.channel()
print "4"
channel.queue_declare(queue='hello')
print "5"
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print "meh"
connection.close()
