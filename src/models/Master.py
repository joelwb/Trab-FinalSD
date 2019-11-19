# -*- coding: utf-8 -*-

'''
    Class that represents a Master.
'''

from kafka import KafkaProducer, KafkaConsumer
from typing import List
import threading

class Master(threading.Thread):
    slaves_ids: List[int] = []

    def __init__(self):
        super().__init__()
        self._daemon: bool = True
        self._status_consumer = KafkaConsumer("status", bootstrap_servers=["localhost:9092"], consumer_timeout_ms=1000)
        self._reg_consumer = KafkaConsumer("reg", bootstrap_servers=["localhost:9092"])

    def request_status(self, slave_id: int) -> str:
        '''Request the current slave status.'''

        if slave_id not in Master.slaves_ids:
            return None

        producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=str.encode)
        producer.send(f"get_status_{slave_id}", "")
        producer.flush()
        producer.close()

        try:
            status = next(self._status_consumer)
        except Exception as e:
            Master.slaves_ids.remove(slave_id)
            raise Exception(f"Slave ID {slave_id} is killed!")
        
        return status.value.decode()

    def run(self) -> None:
        '''Every slave initialized is added into list.'''

        for reg in self._reg_consumer:
            producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=str.encode)
            slave_id = int(reg.value.decode())

            
            if slave_id not in self.slaves_ids:
                producer.send(f"reg_response_{slave_id}","OK")
                self.slaves_ids.append(slave_id)
            else: 
                producer.send(f"reg_response_{slave_id}", f"Slave ID {slave_id} is already registered!")

            producer.flush()
            producer.close()
