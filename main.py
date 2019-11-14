from master import Master
from slave import Slave
import sys

print("Inicializando o Master!")
m = Master()
m.start()

print("Inicializando os Slaves!")
s1 = Slave("slave 1", 1)
s1.start()

s2 = Slave("slave 2", 2)
s2.start()

print(m.request_status(1))
print(m.request_status(2))

try:
    m.request_status(3)
except Exception:
    print("Deu Certo")

sys.exit()

