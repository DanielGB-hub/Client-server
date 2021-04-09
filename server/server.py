import time
import json
import pickle
import socket
import base64
import threading
from cryptography.fernet import Fernet


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.all_client = []
        self.symmetric_key = None

        # Запускаем прослушивание соединений
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(0)
        threading.Thread(target=self.connect_handler).start()
        print('Сервер запущен!')

    # Обрабатываем входящие соединения
    def connect_handler(self):
        while True:
            client, address = self.server.accept()
            if client not in self.all_client:
                self.all_client.append(client)

                # Отправляем запрос на успешное подключение + раздаем симметричные ключи
                self.get_key()
                payload = ['SERVER_OK', "Вы вошли в чат!", self.symmetric_key]
                client.send(pickle.dumps(payload))
                print(f'{address} -  Подключение к чату!')
                threading.Thread(target=self.message_handler, args=(client,)).start()

            time.sleep(2)

    # Обрабатываем отправленный текст
    def message_handler(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                pickle_dec = pickle.loads(message)
                print(pickle_dec)
            except:
                self.all_client.remove(client_socket)
                break

            # Отправляем зашифрованное сообщение всем клиентам
            if pickle_dec[0] == "ENCRYPT_MESSAGE":
                for client in self.all_client:
                    if client != client_socket:
                        client.send(message)

            # Если клиент отправил запрос на дисконнект
            elif pickle_dec[0] == "EXIT":
                print(f'Клиент {pickle_dec[1]} - разорвал соединение!')
                self.all_client.remove(client_socket)
                break

            time.sleep(1)

    # Генератор сессионного семмитричного ключа
    def get_key(self) -> None:
        if self.symmetric_key is None:
            self.symmetric_key = Fernet.generate_key()


if __name__ == "__main__":
    myserver = Server('127.0.0.1', 5555)