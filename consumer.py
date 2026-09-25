import json
from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092,localhost:9093,localhost:9094',
    'group.id': 'cluster-workers',
})

consumer.subscribe(['events'])

totals  = {}


while True:
    message = consumer.poll(1)
    
    if message is not None:
        print(message.value().decode())