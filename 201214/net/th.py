import threading, time

def f1(num):
    for i in range(1,21):
        print('th'+num+':',i)
        time.sleep(1)

def f2():
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        print('th4:',i)
        time.sleep(1)

def main():
    # 쓰레드 생성. target : 쓰레드가 실행할 함수 args는 함수에 파라미터가 있을때 인자값을 주면됨
    th1 = threading.Thread(target=f1, args="1")
    th1.start()
    th2 = threading.Thread(target=f1, args=("2",))
    th2.start()
    th3 = threading.Thread(target=f1, args=("3",))
    th3.start()

    th4 = threading.Thread(target=f2)
    th4.start()

    for i in range(100, 140,2):
        print('main:',i)
        time.sleep(1)
main()