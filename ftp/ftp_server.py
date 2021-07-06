from socket import *
import os
import sys
import time
import signal


FILE_PATH = "/home/huang/python_lianxi/ftpFile/"
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)

class FtpServer(object):
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.senf("wenjian.weikong".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)

        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.sfile(FILE_PATH + file):
                files = files + file + '#'
        self.connfd.sendall(files.encode())

    def do_get(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'rb')
        except:
            self.connfd.send("wenjianbucunzai".encode())
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        print("wenjainwanbi")

def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print("Listen the port 8000...")

    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("tuichu")
        except Exception as e:
            print("yichang:", e)
            continue

        print("yilianjie,kehuduan:", addr)

        pid = os.fork()
        if pid == 0:
            sockfd.close()
            ftp = FtpServer(connfd)
            while True:
                data = connfd.recv(1024).decode()
                if not data or data[0] == 'Q':
                    connfd.close()
                    sys.exit("tuichu")
                elif data[0] == "L":
                    ftp.do_list()
                elif data[0] == 'G':
                    filename = data.split(' ')[-1]
                    ftp.do_get(filename)
        else:
            connfd.close()
            continue

if __name__ == "__main__":
    main()














