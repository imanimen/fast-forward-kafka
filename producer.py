from confluent_kafka import Producer
import json

producer = Producer({
    'bootstrap.servers': 'localhost:9092'
})


for i in range(100):
    order = {
        'order_id': i,
        'customer_id': i % 10,
        'amount': i * 100
    }
    
    producer.produce('orders', key=str(order['customer_id']), value=json.dumps(order))
    
producer.flush()