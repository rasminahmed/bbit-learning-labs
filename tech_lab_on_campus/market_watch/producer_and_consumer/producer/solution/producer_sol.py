import pika
from producer_interface import mqProducerInterface


class mqProducer(mqProducerInterface):
    def __init__(self, routing_key, exchange_name):
        # Save instance variables
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        # Call setup function
        self.setupRMQConnection()

    def setupRMQConnection(self):
        # Establish connection to RabbitMQ
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq")
        )
        self.channel = self.connection.channel()

        # Declare exchange
        self.channel.exchange_declare(
            exchange=self.exchange_name,
            exchange_type="direct"
        )

    def publishOrder(self, message):
        # Publish UTF-8 encoded message
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message.encode("utf-8")
        )

        # Close channel and connection
        self.channel.close()
        self.connection.close()

