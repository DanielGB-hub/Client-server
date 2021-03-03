#  1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM
#  (JSON instant messaging):

from socket import *
import json

ENCODING = "utf-8"

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect(("localhost", 8007))

    auth_msg = {
        "action": "authenticate",
        "time": 123,
        "user": {
                    "account_name": "C0deMaver1ck",
                    "password": "CorrectHorseBatteryStaple"
        }
    }

    msg = json.dumps(auth_msg)
    s.send(msg.encode(ENCODING))
    data = s.recv(1000000)
    recv_str = data.decode(ENCODING)
    print("Сообщение от сервера: ", recv_str, ", длиной ", len(data), " байт")
    s.close()

    recv_msg = json.loads(recv_str)
    print(f"Parsed msg {recv_msg}")

