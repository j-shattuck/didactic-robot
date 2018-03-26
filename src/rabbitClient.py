# Basic client for interacting with RabbitMQ
from logging import Logger
import pika

class RabbitClient:
    def __init__(self, config, logger):
        logger.debug("Initializing RabbitClient")
        self.__logger = logger
        self.__config = config
        self.__connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.__channel = self.__connection.channel()

    def __initializeConnection(self, config):
        self.__logger.debug("Initializing RabbitMQ connection")
        self.__channel.queue_declare(queue=self.__config['queue_name'])

    def publishMessage(self, exchange, routeKey, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.confirm_delivery()
        channel.basic_publish(exchange=exchange,
                                routing_key=routeKey,
                                body=message,
                                properties=pika.BasicProperties(content_type='text/plain', delivery_mode=1))
        channel.close()

    def close(self):
        self.__logger.debug("Closing Rabbit connection")
        self.__connection.close()