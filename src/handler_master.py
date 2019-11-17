# -*- coding: utf-8 -*-

'''
    Module responsible to initialize the Master instance and asks the operator
    about some slave.
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

            if slave_status == None:
                print("Slave ID {0} was not found".format(slave_id))
            else:
                print("Slave ID {0} is currently {1}".format(slave_id, slave_status.upper()))
        except ValueError:
            print("Error: Invalid value ID. Please insert a valid integer positive number ID.")
        except Exception:
            print("Error: Invalid ID. Please insert a valid one")
        finally:
            print()


if __name__ == "__main__":
    import sys
    sys.tracebacklimit = 1
    main()