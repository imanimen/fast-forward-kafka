from confluent_kafka import Producer
import time

producer = Producer({
    'bootstrap.servers': 'localhost:9092,localhost:9093,localhost:9094',
    'acks': 'all',
})


counter = 0

while True:
    producer.produce('events', value=str(counter))
    producer.flush()
    
    print(counter, 'was sent')
    counter += 1
    
    time.sleep(1)