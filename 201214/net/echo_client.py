import socket

HOST = '192.168.55.153'
PORT = 9999

#통신할 소켓 오픈
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#서버 accept()에 연결요청. server ip, port
client_socket.connect((HOST, PORT))

while True:
    msg = input('msg:')
    client_socket.sendall(msg.encode(encoding='utf-8'))

    data = client_socket.recv(1024)
    print('Received', data.decode())
    if msg=='/stop':
        break

client_socket.close()
