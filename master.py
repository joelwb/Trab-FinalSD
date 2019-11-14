from kafka import KafkaProducer, KafkaConsumer
import threading


class Master(threading.Thread):

    slaves_ids = []

    def __init__(self):
        super().__init__()

        self.daemon = True

        self.status_consumer = KafkaConsumer("status", bootstrap_servers=["localhost:9092"])
        self.reg_consumer = KafkaConsumer("reg", bootstrap_servers=["localhost:9092"])

    def request_status(self, slave_id: int):
        if slave_id not in self.slaves_ids:
            raise Exception("Não existe um slave registrado com esse id!")

        producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=str.encode)
        producer.send(f"get_status_{slave_id}", "")
        producer.flush()
        producer.close()

        for status in self.status_consumer:
            return status.value.decode()

    def run(self):
        for reg in self.reg_consumer:
            self.slaves_ids.append(int(reg.value.decode()))
