from confluent_kafka import Producer


producer = Producer({
    'bootstrap.servers': 'localhost:9092'
})


while True:
    message = input('> ')
    producer.produce('test', value=message)
    producer.flush()