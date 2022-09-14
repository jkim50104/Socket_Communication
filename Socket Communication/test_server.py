import socket


# 소켓 객체 생성 
# AF(Address Family): 주소 체계(보통 IP, AF_INET=IPv4, AF_INET6=IPv6), Socket Type: SOCK_STREAM과 SOCK_DGRAM만이 주로 사용
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 생성한 소켓 bind
# 클라이언트의 경우 불필요 서버 운용시 필수, 생성된 소켓의 번호와 실제 AF를 연결
# 튜플 argument 전달, ("AF(보통 ip)", port), ""=INADDR_ANY => 모든 인터페이스와 연결하고 싶다면 빈 문자열, 반대로 브로드캐스트를 하고 싶다면 "" 입력
# 8080번 포트에서 모든 인터페이스에게 연결하도록 한다
port = 8080
serverSock.bind(('127.0.0.1', port))
print("--Server opened--")

# 상대방의 접속을 기다리는 단계
# argument는 몇개의 동시접속까지 허용할 것인가. default의 경우 파이썬이 자의적으로 판단해서 임의의 숫자로 listen
# 얘도 서버소켓에서만 사용
serverSock.listen(1)
print(f"--Waiting for clients in port: {port}--")

# 접속 대기 수락, 누군가 있어 결과값 리턴(새로운 소켓, 상대방 AF)
connectionSock, addr = serverSock.accept()
print(f"--Client: {addr} accepted--")

# 문자열 전송, encode() = 문자열을 byte로 변환해주는 함수
send_msg = "Welcome to R-Biz Server"
connectionSock.send(send_msg.encode("utf-8"))

# 문자열 수신, accept()와 같이 문자열 수신 될때까지 파이썬 코드 대기
recv_msg = connectionSock.recv(1024)
print(f"Client: {recv_msg.decode('utf-8')}")

#소켓에서 주고 받는 데이터는 byte이므로, 굳이 문자열을 주고 받지 않아도 된다. 예를 들어 이미지 파일이나 동영상 파일을 읽어서 1024byte 단위로 전송을 해도 가능