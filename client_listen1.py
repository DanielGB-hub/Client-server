from socket import *
import sys

ENCODING = "utf-8"

PLACE = ("localhost", 8888)


def client():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(PLACE)
        while True:
            receive = sock.recv(1024).decode(ENCODING)
            if receive:
                print("Ответ: ", receive)


if __name__ == "__main__":
    client()
