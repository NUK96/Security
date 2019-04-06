#coding:utf-8

from socket import *
from threading import Thread

def delClient(newSocket,addr):
    while True:
        recvData = newSocket.recv(2048)
        if len(recvData) > 0:
            print("{}:{}".format(str(addr),recvData))
        else:
            print("客户端已经关闭了")
            break
        newSocket.close()

def main():
    serSocket = socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    serSocket.bind(('10.7.68.9',8899))
    serSocket.listen(5)
    
    try:
        while True:
            print("-------主进程，，，等待新客户的到来------")
            newSocket,addr = serSocket.accept()
            print("------主进程，，接下来创建一个新线程负责数据处理{}--------".format(str(addr)))
            client = Thread(target=delClient(),args=(newSocket,addr))
            client.start()
    finally:
        serSocket.close()
        
 
if __name__ == "__main__":
    main()