
import socket
import threading
import time
from util import *


serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#192.168.1.17 연구실 ip
port = 8080
serverSock.bind(('127.0.0.1', port))
print("--Server opened--")

serverSock.listen(1)
print(f"--Waiting for clients in port: {port}--")

connectionSock, addr = serverSock.accept()
print(f"--Client: {addr} accepted--")

#target = 실제로 실행할 함수, 함수에 전달할 인자 args(주의: 튜플로 인자를 전달해야하는데 인자가 하나여도 (var)식으로 입력하면 var로 인식 (var, )로 입력해야 튜플로 인식)
e = [0]
sender = threading.Thread(target=send, args=(connectionSock, e))
receiver = threading.Thread(target=receive, args=(connectionSock, ))

sender.start()
receiver.start()

while True:
    if e[0]:
        serverSock.close()
        print("--Server Closed--")
        break
    time.sleep(1)
    #pass