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
    master.daemon = True
    master.start()

    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # bind to the port
    serversocket.bind(("localhost", 9998))

    # queue up to 5 requests
    serversocket.listen(5)                                          
    
    print("Server is running...\n")

    while True:
        # establish a connection
        try:
            print("Waiting for operator client request...")
            clientsocket, addr = serversocket.accept()      
        except KeyboardInterrupt:
            serversocket.close()
            break

        slave_id = int(clientsocket.recv(1024).decode())

        try:
            print("Stablished operator request.")
            slave_status = master.request_status(slave_id)

            if slave_status == None:
                clientsocket.send("Slave ID {0} was not found".format(slave_id).encode())
            else:
                clientsocket.send("Slave ID {0} is currently {1}".format(slave_id, slave_status.upper()).encode())
            print("Operator request successfully responded.")
        except ValueError:
            clientsocket.send("Error: Invalid value ID. Please insert a valid integer positive number ID.".encode())
            print("Operator request was not successfully responded")
        except Exception as e:
            clientsocket.send(str(e).encode())
            print("Operator request was not successfully responded")
        finally:
            clientsocket.close()
            print("Finished operator client connection.\n")


if __name__ == "__main__":
    sys.tracebacklimit = 1
    main()
    sys.exit(0)
