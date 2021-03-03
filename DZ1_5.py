# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
# из байтовового в строковый тип на кириллице.
import subprocess
print('Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты\n'
      'из байтовового в строковый тип на кириллице')

args = []

with open('DZ1_5.txt') as file:
    for el in file.read().splitlines():
        args = ['ping', el]
        print(args)

        subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        i = 0
        for line in subproc_ping.stdout:
            i += 1
            if i < 10:  # счетчик для остановки вывода пинга и перехода к следующему адресу (у меня Windows, и счетчик нужен для ubuntu)
                line = line.decode('cp866').encode('utf-8')
                print(line.decode('utf-8'))

