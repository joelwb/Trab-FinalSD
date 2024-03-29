import socket

while True:
    try:
        slave_id: int = int(input("Insert the slave id you would like to know about it: "))
    except KeyboardInterrupt:
        break
    except Exception:
        print("Error: Invalid value ID. Please insert a valid integer positive number ID.")
        continue

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # connection to hostname on the port.
    s.connect(("localhost", 9999))

    s.send(str(slave_id).encode())
    print(s.recv(1024).decode())
    print()
