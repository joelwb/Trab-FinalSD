# -*- coding: utf-8 -*-

'''
    Module responsible to initialize the Slaves based on parameters in terminal
    (id and name).
'''

from models.Slave import Slave
from typing import List
import sys

def main(args: List[str]) -> None:
    try:
        slave_id: int = int(args[1])
        slave_name: str = args[2] if args.__len__() >= 3 else "Slave {0}".format(slave_id)
        slave: Slave = Slave(slave_id, slave_name)
        slave.start()
        print("------Woke up!------")
        print(slave)
    except IndexError:
        print("Error: You must pass the slave's ID as argument in terminal.")        
    except ValueError:
        print("Error: Cannot instance slave from this type of ID. Please enter a positive integer ID.")
    except Exception:
        print("Error: There was an error while creating slave.")
    else:
        print()


if __name__ == "__main__":
    main(sys.argv)