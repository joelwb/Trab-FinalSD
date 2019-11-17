# -*- coding: utf-8 -*-

'''
    Module responsible to initialize the Slaves
'''

from models.Slave import Slave
from typing import List

def main(args: List[str]) -> None:
    try:
        slave_id: int = int(args[0])
        slave_name: str = args[1] if args.__len__() > 2 else "Slave {0}".format(slave_id)
        slave: Slave = Slave(slave_id, slave_name)
        slave.start()
    except ValueError:
        print("Cannot instance slave from this type of ID. Please enter a integer ID")
    except IndexError:
        print("You must pass the slave's ID as argument in terminal")
    except Exception:
        print("Error while creating slave")


if __name__ == "__main__":
    import sys
    main(sys.argv)