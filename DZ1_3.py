"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable
-------------
10.0.0.1
10.0.0.2
Unreachable
-------------
10.0.0.3
10.0.0.4
"""

from tabulate import tabulate
import ipaddress
import subprocess
import platform

tuples_list = []


def host_range_ping(ip_start, ip_end):
    try:
        ip1 = ipaddress.ip_address(ip_start)
        ip2 = ipaddress.ip_address(ip_end)

        while ip1 <= ip2:
            ping_str = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", ping_str, "1", str(ip1)]

            try:
                if subprocess.check_output(command, shell=True).decode('cp866'):  # утилита ping проверяет адрес
                    tuples_list.append((ip1, "Reachable"))

            except:
                tuples_list.append((ip1, "Unreachable"))
            ip1 = ip1 + 1

    except:
        print(f"Ошибка ввода данных")
    print(tabulate(tuples_list))


print("Данный скрипт проверит доступность диапазона списка адресов и выведет их в таблицу"
      "(это может занять некоторое время): ")
ip_start = str(input("Введите начальный ip адрес (например, 217.69.139.200): "))
ip_end = str(input("Введите конечный ip адрес (например, 217.69.139.220): "))
host_range_ping(ip_start, ip_end)
