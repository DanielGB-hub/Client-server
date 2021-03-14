from socket import *
import click
import time
import json
import logging
import log.client_log_config
from log.log_decorator_config import log

ENCODING = "utf-8"


def get_time_fun():
    t = int(time.time())
    return t


@log  # конфиг лежит в папке log, сам лог пишется в файл trace.log
def make_auth_message(user, password, get_time_fun):
    msg_time = get_time_fun()
    data = {
        "action": "authenticate",
        "time": msg_time,
        "user": {
            "account_name": user,
            "account_password": password
        }
    }
    return json.dumps(data)

@log
def make_presence_message(user, password, get_time_fun):
    msg_time = get_time_fun()
    data = {
        "action": "presence",
        "time": msg_time,
        "type": "status",
        "user": {
            "account_name": user,
            "account_password": password
        }
    }
    return json.dumps(data)

@log
def make_quit_message(user, password, get_time_fun):
    msg_time = get_time_fun()
    data = {
        "action": "quit",
        "time": msg_time,
        "type": "exit",
        "user": {
            "account_name": user,
            "account_password": password
        }
    }
    return json.dumps(data)


@click.command()
@click.option("-port", default=7777, )
@click.option("-addr", default="127.0.0.1", help="Адрес хоста (default=localhost)")
@log
def run_client(port, addr):
    clt_log = logging.getLogger("client_log")
    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.connect((addr, port))
        except Exception as e:
            clt_log.exception(str(e))
        clt_log.debug("Соединение с сервером")
        msg = make_auth_message("C0deMaver1ck", "CorrectHorseBatteryStaple", get_time_fun)
        clt_log.debug("Создана форма аутентификации")
        try:
            s.send(msg.encode(ENCODING))
            clt_log.debug("Форма аутентификации отправлена на сервер")
        except Exception as e:
            clt_log.exception(str(e))
        try:
            data = s.recv(1000000)
            clt_log.debug("Получен ответ от сервера")
        except Exception as e:
            clt_log.exception(str(e))
        data = json.loads(data)
        if data["response"] == 200:
            msg2 = make_presence_message("C0deMaver1ck", "CorrectHorseBatteryStaple", get_time_fun)
            clt_log.debug("Создана форма presence")
            try:
                s.send(msg2.encode(ENCODING))
                clt_log.debug("Форма presence отправлена на сервер")
            except Exception as e:
                clt_log.exception(str(e))
            time.sleep(5)

            msg3 = make_quit_message("C0deMaver1ck", "CorrectHorseBatteryStaple", get_time_fun)  # отключаемся от сервера
            s.send(msg3.encode(ENCODING))
        else:
            clt_log.exception("Ответ сервера не корректный")


if __name__ == "__main__":
    run_client()
