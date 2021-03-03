#  1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
#  осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
#  и формирующий новый «отчетный» файл в формате CSV

# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
# их открытие и считывание данных.
#
# В этой функции из считанных данных необходимо с помощью регулярных выражений
# извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
#
# Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка —
# например, os_prod_list, os_name_list, os_code_list, os_type_list.
#
# В этой же функции создать главный список для хранения данных отчета — например, main_data —
# и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
# (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().
import os
import re
import csv


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы:', 'Название ОС:', 'Код продукта:', 'Тип системы:']]
    fds = sorted(os.listdir())  # смотрим содержимое каталога
    for txt in fds:  # окрывает файлы вида info_№.txt
        if re.match(r'info_\d+(.txt)\b', txt):
            with open(txt, encoding='utf-8') as file:
                for el in file.read().splitlines():
                    print(f'Содржимое файла {txt}:\n {el}\n')  # необязательный код, для наглядности

                    # Первый вариант: выводим все значения полей в один список, но расположение данных в
                    # файлах info_№.txt должно быть строго по форме.

                    result = re.findall(': (.+?)[,;]', el)
                    os_prod_list.append(result[0])  # распределяем данные по спискам
                    os_name_list.append(result[1])
                    os_code_list.append(result[2])
                    os_type_list.append(result[3])
                    main_data.append(result)  # добавляем список значений для main_data -> .csv

                    # Второй вариант: для уверенного поиска зададим фильтры явно

                    # str1 = re.findall('Изготовитель системы: (.+?)[,;]', el)
                    # os_prod_list.append(str1[0])
                    # str2 = re.findall('Название ОС: (.+?)[,;]', el)
                    # os_name_list.append(str2[0])
                    # str3 = re.findall('Код продукта: (.+?)[,;]', el)
                    # os_code_list.append(str3[0])
                    # str4 = re.findall('Тип системы: (.+?)[,;]', el)
                    # os_type_list.append(str4[0])
                    # main_data.append(os_prod_list)  # добавляем списки значений для main_data -> .csv
                    # main_data.append(os_name_list)
                    # main_data.append(os_code_list)
                    # main_data.append(os_type_list)

    print(f'Содержимое списка os_prod_list: {os_prod_list}')  # необязательный код, для наглядности
    print(f'Содержимое списка os_name_list: {os_name_list}')  #
    print(f'Содержимое списка os_code_list: {os_code_list}')  #
    print(f'Содержимое списка os_type_list: {os_type_list}')  #
    return main_data


def write_to_csv():
    with open('write_to_csv.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in get_data():
            f_n_writer.writerow(row)

    print('\nСодержимое файла write_to_csv.csv:\n')
    with open('write_to_csv.csv') as f_n:
        print(f_n.read())


write_to_csv()

