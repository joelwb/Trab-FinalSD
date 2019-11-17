from kafka import KafkaProducer
import json
import pprint

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    api_version=(0, 10, 1))

producer.send('linuxhint', {'topic': 'kafka'})

metrics = producer.metrics()
pprint.pprint(metrics)