"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний
октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""

import ipaddress
import subprocess
import platform


def host_range_ping(ip_start, ip_end):
    try:
        ip1 = ipaddress.ip_address(ip_start)
        ip2 = ipaddress.ip_address(ip_end)

        while ip1 <= ip2:
            ping_str = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", ping_str, "1", str(ip1)]

            try:
                if subprocess.check_output(command, shell=True).decode('cp866'):  # утилита ping проверяет адрес
                    print(f"Адрес {ip1} - узел доступен")

            except:
                print(f"Адрес {ip1} - узел недоступен")
            ip1 = ip1 + 1

    except:
        print(f"Ошибка ввода данных")


print("Данный скрипт проверит доступность диапазона списка адресов: ")
ip_start = str(input("Введите начальный ip адрес (например, 217.69.139.200): "))
ip_end = str(input("Введите конечный ip адрес (например, 217.69.139.220): "))
host_range_ping(ip_start, ip_end)

