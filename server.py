#coding:utf-8

from socket import *
from threading import Thread

def recv(newsocket):
    while True:
        rdata = newsocket.recv(2048)
        print(">>"+rdata.decode("utf-8"))

def send(newsocket):
    while True:
        sdata = input(">>")
        newsocket.send(sdata.encode("utf-8"))


def main():
    s = socket(AF_INET,SOCK_STREAM)
    s.bind(('',7788))
    s.listen(5)
    while True:
        newsocket,address = s.accept()
        tr = Thread(target=recv,args=(newsocket,))
        ts = Thread(target=send,args=(newsocket,))

        tr.start()
        ts.start()
        
        tr.join()
        ts.join()
        
if __name__ == "__main__":
    main()