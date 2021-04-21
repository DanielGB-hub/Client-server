"""
4. Продолжаем работать над проектом «Мессенджер»:
Реализовать скрипт, запускающий два клиентских приложения: на чтение чата и на запись в него.
Уместно использовать модуль subprocess);
Реализовать скрипт, запускающий указанное количество клиентских приложений.

"""
import os
import subprocess
import psutil
import time


all_processes = []
start = int(input("Данный скрипт запустит клиенты мессенджера. Имена пользователей будут в виде User{номер клиента}.\n"
                  "Введите количество клиентов: "))

client_path = os.getcwd() + "\client.py"

i = 1
while i <= start:
    client_name = "client" + f"{str(i)}"
    print(client_name)
    client_name = f"python {client_path} -n User{i}"
    all_processes.append(subprocess.Popen(f"{client_name}", stdout=subprocess.PIPE, shell=True))
    i = i + 1
    time.sleep(0.2)


print(all_processes)
print(*(prog for prog in psutil.process_iter() if prog.name() == "python.exe"))


stop = input("Для остановки сервера и клиентов становите данный процесс \n")

