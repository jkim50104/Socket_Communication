from pydoc import cli
import socket
import threading
import time
from util import *


clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("--New Client--")

port = 8080
clientSock.connect(('127.0.0.1', port))
print("--Connection Complete--")

e = [0]
sender = threading.Thread(target=send, args=(clientSock, e))
receiver = threading.Thread(target=receive, args=(clientSock, ))

sender.start()
receiver.start()

while True:
    if e[0]:
        clientSock.close()
        print("--Client out--")
        break
    time.sleep(1)
    #pass