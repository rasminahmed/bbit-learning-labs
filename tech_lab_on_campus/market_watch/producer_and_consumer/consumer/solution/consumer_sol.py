In the solution directory, create a file named consumer_sol.py
Write your code in the consumer_sol.py file
Create a class named mqConsumer
Your class should inherit from our mqConsumerInterface.
Constructor:Save the three variables needed to instantiate the class.
Constructor: Call the setupRMQConnection function.
setupRMQConnection Function: Establish connection to the RabbitMQ service, declare a queue and exchange, bind the binding key to the queue on the exchange and finally set up a callback function for receiving messages
onMessageCallback: Print the UTF-8 string message and then close the connection.
startConsuming: Consumer should start listening for messages from the queue.
Del: Close Connection and Channel.


class mqConsumerInterface:
    def __init__(
        self, binding_key: str, exchange_name: str, queue_name: str
    ) -> None:
        # Save parameters to class variables

        # Call setupRMQConnection
        pass

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service

        # Establish Channel

        # Create Queue if not already present

        # Create the exchange if not already present

        # Bind Binding Key to Queue on the exchange

        # Set-up Callback function for receiving messages
        pass

    def on_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        # Acknowledge message

        #Print message (The message is contained in the body parameter variable)

        pass

    def startConsuming(self) -> None:
        # Print " [*] Waiting for messages. To exit press CTRL+C"

        # Start consuming messages
        pass
    
    def __del__(self) -> None:
        # Print "Closing RMQ connection on destruction"
        
        # Close Channel

        # Close Connection
        
        pass

class mqConsumer(mqConsumerInterface):
  
  def init_ (self, key, eName, qName)
    self.binding_key: key
    self.exchange_name: eName
    self.queueName: qName
  setupRMQConnection(self)
  conParams = pika.URLParameters(os.environ['AMQP_URL'])
  connection = pika.BlockingConnection(parameters=conParams)
  channel = connection.channel()
  channel.queue_declare(queue='Test')


  
