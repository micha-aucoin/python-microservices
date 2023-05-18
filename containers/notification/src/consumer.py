import os
import sys
import time

import pika
from send import email
from src import settings


def main():
    # rabbitmq connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.rabbitmq_host)
    )
    channel = connection.channel()

    def callback(ch, method, properties, body):
        try:
            err = email.notification(body.decode())
            if err:
                print(f"Error occurred: {err}")
                ch.basic_nack(delivery_tag=method.delivery_tag)
            else:
                ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue=settings.mp3_queue,
        on_message_callback=callback,
    )

    print("Waiting for messages. To exit press CTRL+C")

    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
