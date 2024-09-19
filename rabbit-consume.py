import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (ensure the queue already exists)
# channel.queue_declare(queue='notification_worker_queue')

# Define a callback function to process the message
def callback(ch, method, properties, body):
    print(f" [x] Notification Received: {body.decode()}")

# Set up the consumer to listen to the queue
channel.basic_consume(queue='notification_worker_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for notifications. To exit press CTRL+C')

# Start consuming messages
channel.start_consuming()
