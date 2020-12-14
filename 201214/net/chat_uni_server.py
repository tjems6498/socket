import threading, socket

class UniServer:
    ip = 'localhost'
    port = 5555

    def __init__(self):
        self.server_soc = None # 서버 소켓(대문)
        self.client_soc = None # 클라이언트와 1:1 통신 소켓

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((UniServer.ip, UniServer.port))
        self.server_soc.listen()

    def sendMsg(self):
        while True:
            msg = input('>>>')
            msg = msg.encode(encoding='utf-8')
            self.client_soc.sendall(msg)
            if msg == '/stop':
                break

    def recvMsg(self):
        while True:
            data = self.client_soc.recv(1024)
            msg = data.decode(encoding='utf-8')
            print("상대방 메시지:",msg)
            if msg == '/stop':
                break

    def run(self):
        self.open()
        self.client_soc, addr = self.server_soc.accept() #accept가 반복문이 아니라 1개니까 클라이언트는 1명만 가능

        th1 = threading.Thread(target=self.sendMsg)
        th1.start()
        th2 = threading.Thread(target=self.recvMsg)
        th2.start()

    def close(self):
        self.client_soc.close()
        self.server_soc.close()

def main():
    server = UniServer()
    server.run()

main()