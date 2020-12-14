import socket, threading

def echo_msg(soc):#soc:접속한 클라이언트 1명과 1:1통신하는 소켓
    while True:
        data = soc.recv(1024)  # recv(크기):소켓에서 메시지 읽음
        msg = data.decode()  # 인코딩된 메시지를 원래대로 디코딩함
        print('Received from', msg)
        soc.sendall(data)
        if msg == '/stop':
            break
    #쓰레드 종료
    print('쓰레드 종료')

def main():
    HOST = 'localhost'
    PORT = 9999
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print('server start')
    while True:
        client_socket, addr = server_socket.accept()
        print('Connected by', addr)

        th = threading.Thread(target=echo_msg, args=(client_socket, ))
        th.start()

    server_socket.close()

main()
