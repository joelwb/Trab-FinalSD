# -*- coding: utf-8 -*-

'''
    Class that represents a Slave.
'''

from kafka import KafkaProducer, KafkaConsumer
from datetime import datetime
import threading

class Slave(threading.Thread):

    def __init__(self, id: int, name: str):
        super().__init__()
        self._daemon: bool = True
        self.id: int = id
        self.name: str = name
        self._consumer = KafkaConsumer(f"get_status_{self.id}", bootstrap_servers=["localhost:9092"])
        self.__make_reg(id)

    def __make_reg(self, id: int) -> None:
        producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=str.encode)
        producer.send("reg", str(id))
        #producer.flush()
        producer.close()

    def run(self) -> None:
        for msg in self._consumer:
            producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=str.encode)
            seg_atual = datetime.now().second

            status = "Not Working" if seg_atual >= 30 else "Working"
            producer.send("status", status)
            #producer.flush()
            producer.close()