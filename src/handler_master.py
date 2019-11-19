# -*- coding: utf-8 -*-

'''
    Module responsible to initialize the Master instance and asks the operator
    about some slave.
'''

import socket
from models.master import Master
import sys


def main() -> None:
    master: Master = Master()
    master.start()

    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # bind to the port
    serversocket.bind(("localhost", 9977))

    # queue up to 5 requests
    serversocket.listen(5)                                          
    
    while True:
        # establish a connection
        try:
            clientsocket, addr = serversocket.accept()      
        except KeyboardInterrupt:
            break

        slave_id = int(clientsocket.recv(1024).decode())

        try:
            slave_status = master.request_status(slave_id)

            if slave_status == None:
                clientsocket.send("Slave ID {0} was not found".format(slave_id).encode())
            else:
                clientsocket.send("Slave ID {0} is currently {1}".format(slave_id, slave_status.upper()).encode())
        except ValueError:
            clientsocket.send("Error: Invalid value ID. Please insert a valid integer positive number ID.".encode())
        except Exception as e:
            clientsocket.send(str(e).encode())
        finally:
            clientsocket.close()


if __name__ == "__main__":
    sys.tracebacklimit = 1
    main()
    sys.exit(0)
