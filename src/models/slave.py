# -*- coding: utf-8 -*-

'''
    Class that represents a Slave.
'''

from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
from datetime import datetime, timedelta
from enum import Enum
import threading
import random

class Status(Enum):
    NOT_WORKING = 0, 'Not Working'
    WORKING = 1, 'Working'

    def __str__(self):
        return self.value[1]


class Slave(threading.Thread):

    def __init__(self, id: int, name: str):
        if (id <= 0): raise ValueError("ID must be a positive integer")
        
        super().__init__()
        self._daemon: bool = True
        self._id: int = id
        self._name: str = name
        self._status_up_time: datetime = datetime.now()
        self._actual_status: Status = self.__set_status()
        self._consumer = KafkaConsumer(f"get_status_{self.id}", bootstrap_servers=["localhost:9092"])
        self._reg_consumer = KafkaConsumer(f"reg_response_{self.id}", bootstrap_servers=["localhost:9092"], consumer_timeout_ms=5000)
       
        try:
            admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092")
            admin_client.create_topics([NewTopic(f"reg_response_{self.id}", 1, 1), NewTopic(f"get_status_{self.id}", 1, 1)])
        except:
            pass

        self.__make_reg(id)

    def __str__(self) -> str:
        return "- ID: {}\n- Name: {}\n- Status: {}\n- Time: {}\n".format(self._id, self._name, str(self._actual_status), self._status_up_time.strftime("%Y-%m-%d %H:%M:%S"))

    @property
    def id(self) -> int:
        return self._id

    @property
    def status(self) -> str:
        return str(self._actual_status)

    def __make_reg(self, id: int) -> None:
        producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=str.encode)
        producer.send("reg", str(id)).get(timeout=5)
        producer.close()

        try:
            response = next(self._reg_consumer).value.decode()
        except:
            raise Exception("Master was not found!")

        if response != "OK":
            raise Exception(response)


    def __set_status(self) -> Status:
        '''
            Set the status of the slave based on the hour. To set the status follow the rules below:
            * 00:00:00 to 05:59:59 - Working;
            * 06:00:00 to 11:59:59 - Not Working;
            * 12:00:00 to 17:59:59 - Working;
            * 18:00:00 to 23:59:59 - Not Working;
        '''
        current_datetime: datetime = datetime.now() #+ timedelta(hours=random.randint(0, 24))
        self._status_up_time = current_datetime

        if ((current_datetime.hour >= 0 and current_datetime.hour < 6) or 
            (current_datetime.hour >= 12 and current_datetime.hour < 18)):
            self._actual_status = Status.WORKING
        else:
            self._actual_status = Status.NOT_WORKING

        return self._actual_status


    def run(self) -> None:
        for msg in self._consumer:
            producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=str.encode)
            status: str = str(self.__set_status())

            print("----The Master is requering my info----")
            print(self)
            
            producer.send("status", status).get(timeout=5)
            producer.close()
