# -*- coding: utf-8 -*-

'''
    Module responsible to initialize the Slaves based on parameters in terminal
    (id and name).
'''

from models.slave import Slave
from typing import List
import sys


def main(args: List[str]) -> None:
    try:
        slave_id: int = int(args[1])
        slave_name: str = args[2] if args.__len__() >= 3 else "Slave {0}".format(slave_id)
        slave: Slave = Slave(slave_id, slave_name)
        slave.daemon = True
        print("------Woke up!------")
        print(slave)
        
        slave.start()
        slave.join()
    except KeyboardInterrupt:
        pass
    except IndexError:
        print("Error: You must pass the slave's ID as argument in terminal.")        
    except ValueError:
        print("Error: Cannot instance slave from this type of ID. Please enter a positive integer ID.")
    except Exception as e:
        print(e)
    else:
        print()


if __name__ == "__main__":
    main(sys.argv)