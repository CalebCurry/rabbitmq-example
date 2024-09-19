import time
import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the exchange and the routing key
exchange_name = 'notifications_exchange'
routing_key = 'routing_key'

# Declare the exchange (ensure it's the same as created in RabbitMQ)
channel.exchange_declare(exchange=exchange_name, exchange_type='direct')


while True:

    # Message to send
    message = "New user sign-up notification!"

    # Publish the message to the exchange with a routing key
    channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

    print(f" [x] Sent: {message}")

    time.sleep(1)

# Close the connection
connection.close()
