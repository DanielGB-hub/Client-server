"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().

"""
import ipaddress
import sys
import locale
import subprocess
import platform
import socket


def host_ping(scan_list):
    for el in scan_list:
        try:
            host = socket.gethostbyname(el)
            host_ip = str(ipaddress.ip_address(host))  # ip-адрес сетевого узла создается с помощью функции ip_address()
            ping_str = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", ping_str, "1", host_ip]
            if subprocess.check_output(command, shell=True).decode('cp866'):  # утилита ping проверяет адрес
                print(f"Адрес {el} ({host_ip}) - узел доступен")

        except:
            print(f"Адрес {el} - узел недоступен")


print("Данный скрипт проверит доступность списка адресов: "
      "google.com, yandex.ru, mail.ru, goooo5ogle.com и 193.100.120.10: ")
host_list = ["google.com", "yandex.ru", "mail.ru", "goooo5ogle.com", "193.100.120.10"]  # список адресов
host_ping(host_list)




