#  1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM
#  (JSON instant messaging):

from socket import *
import click
import json
from contextlib import closing

ENCODING = "utf-8"


def form_auth_server_msg():
    msg = {
        "response": 200,
        "alert": "Ok!"
    }
    return json.dumps(msg)


@click.command()
@click.option("-port", default=7777, help="порт (default=7777)")
@click.option("-addr", default="", help="слушаемый ip адрес (default=все адреса)")
def run_server(port, addr):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((addr, port))
        s.listen()

        while True:
            client, addr = s.accept()
            with closing(client):
                while True:
                    data = client.recv(1000000)
                    recv_str = data.decode(ENCODING)
                    # print(f"\nСообщение: {recv_str}, было отправлено клиентом: {addr}\n")
                    recv_msg = json.loads(recv_str)

                    if "action" in recv_msg and recv_msg["action"] == "authenticate":
                        print(f'Статус клиента {addr}: {recv_msg["action"]}')
                        msg = form_auth_server_msg()
                        client.send(msg.encode(ENCODING))

                    if "action" in recv_msg and recv_msg["action"] == "presence":
                        print(f'Статус клиента {addr} поменялся: {recv_msg["action"]}')

                    elif "action" in recv_msg and recv_msg["action"] == "quit":
                        print(f'Статус клиента {addr} поменялся: {recv_msg["action"]}')
                        print("Клиент отключился от сервера, соедиение закрыто")
                        break


if __name__ == "__main__":
    run_server()

