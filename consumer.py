import json
from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-workers',
})

consumer.subscribe(['orders'])

totals  = {}


while True:
    message = consumer.poll(1)
    
    if message is not None:
        order = json.loads(message.value().decode())
        
        customer_id = order['customer_id']
        if customer_id in totals:
            totals[customer_id] += order['amount']
        else:
            totals[customer_id] = order['amount']
        print('Customer:', customer_id, 'Total:', totals[customer_id])
        print(message.partition())