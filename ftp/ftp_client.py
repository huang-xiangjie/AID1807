from socket import *
import sys
import time


class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("wanbi\n")
        else:
            print(data)

    def do_get(self, filename):
        self.sockfd.send(('G' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            fd = open(filename, 'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("%s wanbi\n" % filename)
        else:
            print(data)
    def do_quit(self):
        self.sockfd.send(b'Q')

def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except:
        print("lianjie.shibai")
        return

    ftp = FtpClient(sockfd)
    while True:
        print("=================mingling==============")
        print("*******************list***************")
        print("*******************get file****************")
        print("*****************put file****************")
        print("*****************quit****************")
        print("=========================================")

        cmd = input("shuru>>")

        if cmd.strip() == 'list':
            ftp.do_list()

if __name__ == "__main__":
    main()
















