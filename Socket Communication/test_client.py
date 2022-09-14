import socket


clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("--New Client--")

clientSock.connect(('127.0.0.1', 8080))
print("--Connection Complete--")

send_msg = "Hi, I'm new to this server. :)"
clientSock.send(send_msg.encode("utf-8"))

recv_msg = clientSock.recv(1024)
print(f"Server: {recv_msg.decode('utf-8')}")
