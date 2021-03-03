# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.
import locale


with open('test_file.txt') as f_n:
    #for el_str in f_n:
    def_coding = locale.getpreferredencoding()
    print(f'Открываем файл test_file.txt:\nКодировка по умолчанию:  {def_coding}\n')

print('Принудительно открываем файл в формате Unicode и смотрим его содержимое:\n')
with open('test_file.txt', encoding='utf-8') as f_n1:
    for el_str in f_n1:
            print(el_str, end='')

print('\n')




