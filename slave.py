from kafka import KafkaProducer, KafkaConsumer
from datetime import datetime
import threading


class Slave(threading.Thread):

    def __init__(self, name: str, id: int):
        super().__init__()

        self.daemon = True

        self.id = id
        self.name = name
        self.consumer = KafkaConsumer(f"get_status_{self.id}", bootstrap_servers=["localhost:9092"])

        self.__make_reg()

    def __make_reg(self):
        producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=str.encode)
        producer.send("reg", str(self.id))
        producer.flush()
        producer.close()

    def run(self):

        for msg in self.consumer:
            producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=str.encode)
            seg_atual = datetime.now().second

            status = "Not Working" if seg_atual >= 30 else "Working"
            producer.send("status", status)
            producer.flush()
            producer.close()