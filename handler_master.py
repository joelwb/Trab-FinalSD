# -*- coding: utf-8 -*-

'''
    Module responsible to initialize the Master instance and asks the operator
    about some slave
'''

from models.Master import Master

def main() -> None:
    master: Master = Master()
    master.start()
    ask_operator(master)

def ask_operator(master: Master) -> None:
    while True:
        try:
            slave_id: int = int(input("Insert the slave id you would like to know about it: "))
            slave_status: str = master.request_status(slave_id)
            print("Slave ID: {0} - is current {1}".format(slave_id, slave_status.upper()))
        except ValueError:
            print("Invalid value id. Please insert a valid integer number id.")
        except Exception:
            print("Invalid id. Please insert a valid one")


if __name__ == "__main__":
    main()