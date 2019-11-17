from kafka import KafkaConsumer
from kafka import TopicPartition

print('Making connection.')
consumer = KafkaConsumer(bootstrap_servers='localhost:9092', api_version=(0, 10, 1))

print('Assigning Topic.')
consumer.assign([TopicPartition('linuxhint', 2)])

print('Getting message.')
for message in consumer:
    print("OFFSET: " + str(message[0])+ "\t MSG: " + str(message))