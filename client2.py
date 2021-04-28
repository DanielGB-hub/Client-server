import sys
import json
import time
import socket
import argparse
import logging
import threading
import logs.client_log_config

from configs.default import ACTION, TIME, USER, ACCOUNT_NAME, SENDER, DESTINATION, PRESENCE, RESPONSE, \
    DEFAULT_IP_ADDRESS, DEFAULT_PORT, MESSAGE, MESSAGE_TEXT, ERROR, QUIT,ACCOUNT_PASSWORD, STATUS, TYPE
from configs.client_messages import send_message, receive_message
from decorators.log_decorator import log


# Инициализация клиентского логера
client_logger = logging.getLogger("client")


def get_time_fun():
    t = int(time.time())
    return t


@log  # конфиг лежит в папке logs
def make_presence_msg(account_name, account_password):
    """
    Формирование сообщения о присутствии
    :param account_name: строка псевдонима
    :param account_password: строка пароля
    :return: словарь ответа о присутствии клиента
    """
    out = {
        ACTION: PRESENCE,
        TIME: get_time_fun(),
        TYPE: STATUS,
        USER: {
            ACCOUNT_NAME: account_name,
            ACCOUNT_PASSWORD: account_password
        }
    }

    client_logger.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')

    return out


@log
def make_exit_message(account_name, account_password):
    """
    Формирование сообщения о выходе
    :param account_name: строка псевдонима
    :param account_password: строка пароля
    :return: словарь ответа о выходе клиента
    """
    out = {
        ACTION: PRESENCE,
        TIME: get_time_fun(),
        TYPE: STATUS,
        USER: {
            ACCOUNT_NAME: account_name,
            ACCOUNT_PASSWORD: account_password
        }
    }

    client_logger.debug(f'Сформировано {QUIT} сообщение для пользователя {account_name}')
    return out


@log
def create_client_msg(sock, account_name):
    """
    Формирование и отправка на сервер сообщения клиента
    :param sock: клиентский сокет
    :param account_name: строка псевдонима
    :return message_dict: словарь сообщения клиента
    """

    receiver_name = input('Введите получателя сообщения: ')
    message_str = input('Введите сообщение для отправки: ')

    message_dict = {
        ACTION: MESSAGE,
        TIME: get_time_fun(),
        SENDER: account_name,
        DESTINATION: receiver_name,
        MESSAGE_TEXT: message_str
    }

    client_logger.debug(f'Сформировано сообщение: {message_dict}')

    try:
        send_message(sock, message_dict)
        client_logger.info(f'Отправлено сообщение для пользователя {receiver_name}')
    except Exception:
        client_logger.critical('Потеряно соединение с сервером.')
        sys.exit(1)


@log
def parse_server_msg(sock, user_name):
    """
    Обработчик поступающих сообщений с сервера
    :param sock: клиентский сокет
    :param user_name: имя текущего клиента
    :return:
    """

    while True:
        try:
            message = receive_message(sock)

            # приветственное сообщение
            if RESPONSE in message:
                if message[RESPONSE] == 200:
                    client_logger.debug(f'Получено приветственное сообщение от сервера: {message[RESPONSE]} OK')
                    return f'{message[RESPONSE]} OK'
                elif message[RESPONSE] == 400:
                    client_logger.debug(f'Получено сообщение от сервера: {message[RESPONSE]} {message[ERROR]}')
                    return f'{message[RESPONSE]} {message[ERROR]}'

            # сообщение от другого клиента
            elif ACTION in message and message[ACTION] == MESSAGE and \
                    SENDER in message and DESTINATION in message \
                    and MESSAGE_TEXT in message and message[DESTINATION] == user_name:
                print(f'\n Получено сообщение от пользователя {message[SENDER]}:'
                      f'\n {message[MESSAGE_TEXT]}')
                client_logger.info(f'Получено сообщение от пользователя {message[SENDER]}: {message[MESSAGE_TEXT]}')

            # некорректное сообщение
            else:
                client_logger.error(f'Получено некорректное сообщение с сервера: {message}')

        # ошибка соединения с сервером
        except (OSError, ConnectionError, ConnectionAbortedError, ConnectionResetError, json.JSONDecodeError):
            client_logger.critical(f'Потеряно соединение с сервером.')
            break


@log
def user_controls_cmd(sock, user_name, user_password):
    """
    Обработчик поступающих команд от клиента
    :param sock: клиентский сокет
    :param user_name: имя текущего клиента
    :param user_password: пароль текущего клиента
    :return:
    """
    print("Команда \"message\" для ввода и отправки сообщения, \"quit\" для завершения работы: ")

    while True:
        command = input("Введите команду: ")
        if command == "message":
            create_client_msg(sock, user_name)
        elif command == "quit":
            send_message(sock, make_exit_message(user_name, user_password))
            client_logger.info("Завершение работы по команде пользователя")
            print("Завершение работы")
            time.sleep(0.2)
            break
        else:
            print("Команда не распознана, попробуйте снова. \n"
                  "Команда \"message\" для ввода и отправки сообщения, \"exit\" для завершения работы: ")


@log
def parse_cmd_arguments():
    """
    Парсер аргументов командной строки
    :return: ip-адрес и порт сервера, режим клиента
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", default=DEFAULT_IP_ADDRESS, nargs="?")
    parser.add_argument("-p", default=DEFAULT_PORT, type=int, nargs="?")
    parser.add_argument("-n", "--name", default="User6", nargs="?")
    parser.add_argument("-pw", "--password", default="password6", nargs="?")

    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.a
    port = namespace.p
    name = namespace.name
    password = namespace.password

    if port < 1024 or port > 65535:
        client_logger.critical(f"Попытка запуска клиента с неподходящим номером порта: {server_port} "
                               f"Допустимы адреса с 1024 до 65535. Клиент завершается")
        sys.exit(1)

    return addr, port, name, password


if __name__ == "__main__":
    event = threading.Event()
    print("Запуск клиента")

    server_addr, server_port, client_name, client_password = parse_cmd_arguments()

    if not client_name:
        client_name = input("Введите имя пользователя: ")

    client_logger.info(f"Запущен клиент с парамертами: "
                       f"адрес сервера: {server_addr}, порт: {server_port}, имя пользователя: {client_name}")
    print(f"Запущен клиент с парамертами: "
          f"адрес сервера: {server_addr}, порт: {server_port}, имя пользователя: {client_name}")

    try:

        client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_tcp.connect((server_addr, server_port))
        presence_msg = make_presence_msg(client_name, client_password)  #
        send_message(client_tcp, presence_msg)
        server_answer = parse_server_msg(client_tcp, client_name)

        client_logger.info(f"Установлено соединение с сервером. Ответ сервера: {server_answer}")
        print(f"Установлено соединение с сервером. Ответ сервера: {server_answer}")

    except json.JSONDecodeError:
        client_logger.error("Не удалось декодировать полученную json-строку")
        print("Не удалось декодировать полученную json-строку")
        sys.exit(1)

    except ConnectionRefusedError:
        client_logger.critical(f"Не удалось подключиться к серверу {server_addr}:{server_port}, "
                               f"запрос на подключение отклонён")
        print(f"Не удалось подключиться к серверу {server_addr}:{server_port}, "
              f"запрос на подключение отклонён")

    else:
        # прием сообщений
        receiver = threading.Thread(target=parse_server_msg, args=(client_tcp, client_name))
        #receiver.daemon = True
        receiver.start()

        # отправка сообщений
        user_interface = threading.Thread(target=user_controls_cmd, args=(client_tcp, client_name, client_password)) #
        #user_interface.daemon = True
        user_interface.start()

        client_logger.debug("Процессы запущены")

        while event.is_set():
        #while True:
            time.sleep(1)
            if receiver.is_alive() and user_interface.is_alive():
                continue
            break
        event.set()
        receiver.join()
        user_interface.join()

