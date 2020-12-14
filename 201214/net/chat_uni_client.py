import socket, threading

class UniClient:
    ip = 'localhost'
    port = 5555

    def __init__(self):
        self.client_soc = None

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((UniClient.ip, UniClient.port))

    def sendMsg(self):
        while True:
            msg = input('>>>')
            self.client_soc.sendall(msg.encode(encoding='utf-8'))
            if msg == '/stop':
                break

    def recvMsg(self):
        while True:
            data = self.client_soc.recv(1024)
            msg = data.decode(encoding='utf-8')
            print("상대방 메시지:", msg)
            if msg == '/stop':
                break

    def close(self):
        self.client_soc.close()

    def run(self):
        self.conn()
        th1 = threading.Thread(target=self.sendMsg)
        th1.start()
        th2 = threading.Thread(target=self.recvMsg)
        th2.start()

def main():
    c = UniClient()
    c.run()

main()