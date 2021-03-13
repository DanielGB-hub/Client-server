#  1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM
#  (JSON instant messaging):

from socket import *
import click
import json
from contextlib import closing
import logging
import log.server_log_config

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
    srv_log = logging.getLogger("server_log")
    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.bind((addr, port))
            s.listen()
        except Exception as e:
            srv_log.exception(str(e))
        srv_log.debug(f"Сервер слушает порт {port}")
        while True:
            srv_log.debug("Запуск сервера")
            try:
                client, addr = s.accept()
                srv_log.debug("Установлено соединение с сервером")
            except Exception as e:
                srv_log.exception(str(e))
            with closing(client):
                while True:
                    data = client.recv(1000000)
                    srv_log.debug("Получена форма данных")
                    recv_str = data.decode(ENCODING)
                    # print(f"\nСообщение: {recv_str}, было отправлено клиентом: {addr}\n")
                    recv_msg = json.loads(recv_str)

                    if "action" in recv_msg and recv_msg["action"] == "authenticate":
                        # print(f'Статус клиента {addr}: {recv_msg["action"]}')
                        msg = form_auth_server_msg()
                        srv_log.debug("Создан ответ сервера на форму аутентификации")
                        try:
                            client.send(msg.encode(ENCODING))
                            srv_log.debug("Ответ сервера отправлен клиенту")
                        except Exception as e:
                            srv_log.exception(str(e))

                    if "action" in recv_msg and recv_msg["action"] == "presence":
                        # print(f'Статус клиента {addr} поменялся: {recv_msg["action"]}')
                        srv_log.debug("От клиента получена форма presence")
                    elif "action" in recv_msg and recv_msg["action"] == "quit":
                        # print(f'Статус клиента {addr} поменялся: {recv_msg["action"]}')
                        # print("Клиент отключился от сервера, соедиение закрыто")
                        srv_log.debug("От клиента получена форма quit, соединение закрыто")
                        break


if __name__ == "__main__":
    run_server()

