from socket import *
import click
import time
import json

ENCODING = "utf-8"


def form_auth_message():
    msg_time = int(time.time())
    data = {
        "action": "authenticate",
        "time": msg_time,
        "user": {
            "account_name": "C0deMaver1ck",
            "account_password": "CorrectHorseBatteryStaple"
        }
    }
    return json.dumps(data)


def form_presence_message():
    msg_time = int(time.time())
    data = {
        "action": "presence",
        "time": msg_time,
        "type": "status",
        "user": {
            "account_name": "C0deMaver1ck",
            "account_password": "CorrectHorseBatteryStaple"
        }
    }
    return json.dumps(data)


def form_quit_message():
    msg_time = int(time.time())
    data = {
        "action": "quit",
        "time": msg_time,
        "type": "exit",
        "user": {
            "account_name": "C0deMaver1ck",
            "account_password": "CorrectHorseBatteryStaple"
        }
    }
    return json.dumps(data)


@click.command()
@click.option("-port", default=7777, )
@click.option("-addr", default="127.0.0.1", help="Адрес хоста (default=localhost)")
def run_client(port, addr):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((addr, port))
        msg = form_auth_message()
        s.send(msg.encode(ENCODING))
        data = s.recv(1000000)
        data = json.loads(data)
        if data["response"] == 200:
            msg2 = form_presence_message()
            s.send(msg2.encode(ENCODING))

            time.sleep(5)

            msg3 = form_quit_message()  # отключаемся от сервера
            s.send(msg3.encode(ENCODING))


if __name__ == "__main__":
    run_client()

