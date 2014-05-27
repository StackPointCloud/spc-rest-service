import pika
import logging
import json

logging.basicConfig(filename='message_queue.log',level=logging.INFO)

__all__ = [
    'submit_mq_request'
]

def submit_mq_request(self, data):
	logging.info('STARTING ################')
	logging.info(data)
	logging.info('D###########################')
#	credentials = pika.PlainCredentials('stackpointcloud', 'stackpointcloud')
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))
	channel = connection.channel()
	channel.queue_declare(queue='build')
	json_data = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='build', properties=pika.BasicProperties(content_type='application/json'),body=json_data)
	connection.close()
	return
