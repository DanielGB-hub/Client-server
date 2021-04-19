import json

from configs.default import ENCODING, MAX_PACKAGE_LENGTH


def receive_message(sock):
    """
    Получение сообщения
    :param sock: сокет
    :return: словарь ответа
    """

    encoded_response = sock.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise ValueError
    else:
        raise ValueError


def send_message(sock, message):
    """
    Отправление сообщения
    :param sock: сокет
    :param message: словарь сообщения
    :return: None
    """

    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
