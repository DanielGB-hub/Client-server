#  1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM
#  (JSON instant messaging):

from contextlib import closing
from socket import *
import json

ENCODING = "utf-8"

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(("", 8007))
    s.listen()

    while True:
        client, addr = s.accept()
        with closing(client):
            while True:
                data = client.recv(1000000)
                recv_str = data.decode(ENCODING)
                print("Сообщение: ", recv_str, ", было отправлено клиентом: ", addr)
                recv_msg = json.loads(recv_str)

                if "action" in recv_msg and recv_msg["action"] == "authenticate":
                    msg = {
                        "response": 200,
                        "alert": "Необязательное сообщение/уведомление"
                    }
                    msg = json.dumps(msg)
                    client.send(msg.encode(ENCODING))
                elif "action" in recv_msg and recv_msg["action"] == "quit":
                    print("Client exited")
                    break
