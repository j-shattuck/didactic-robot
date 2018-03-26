# Basic PoC effort to play with python
import argparse
import pika

def main():
    print('hello')
    exchange = ''
    routeKey = 'testqueue'
    message = 'Hellow World'
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.confirm_delivery()
    res = channel.basic_publish(exchange=exchange,
                            routing_key=routeKey,
                            body=message,
                            properties=pika.BasicProperties(content_type='text/plain', delivery_mode=1))
    channel.close()

    if res:
        print("success")
    else:
        print("fail")

if __name__ == '__main__':
    argParser = argparse.ArgumentParser(description = "Run P4 monitor daemon module")
    main()
