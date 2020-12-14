import socket

HOST = '192.168.55.153'  #server ip. localhost. or  127.0.0.1
PORT = 9999         #server port 프로그램을 구분하는 유일한 번호

# 서버 소켓 오픈 -> 클라이언트를 맞기위해서 큰 대문을 열어두는것.
#server socket open. socket.AF_INET:주소체계(IPV4), socket.SOCK_STREAM:tcp  / 다이어그램은 UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#포트 여러번 바인드하면 발생하는 에러 방지 / 필수는 아님
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#바인드:오픈한 소켓에 IP와 PORT 할당
server_socket.bind((HOST, PORT))

#이제 accept할 수 있음을 알림
server_socket.listen()

print('server start')

#accept로 client의 접속을 기다리다 요청시 처리.
#client와 1:1통신할 작은 소켓과 연결된 상대방의 주소 반환
# 쓰레드를 사용하지 않았고, accet가 하나이기때문에 서버에 한명밖에 못들어온다.
# 쓰레드가 홈쇼핑에서 텔레마켓터역할을 한다.
client_socket, addr = server_socket.accept()

print('Connected by', addr)

while True:
    data = client_socket.recv(1024) # recv(크기) :클라이언트가 보낸 메시지를 소켓에서 메시지 읽음
    msg = data.decode() # 인코딩된 메시지를 원래대로 디코딩함
    print('Received from', addr, msg)
    client_socket.sendall(data)
    if msg=='/stop':
        break

client_socket.close()
server_socket.close()
