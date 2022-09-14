


def send(sock, e):
    while True:
        send_msg = input(">>>")
        
        if send_msg == "exit":
            e[0] = 1

        send_msg = send_msg
        sock.send(send_msg.encode("utf-8"))

def receive(sock):
    while True:
        recv_msg = sock.recv(1024)
        print(f"Juno: {recv_msg.decode('utf-8')}")