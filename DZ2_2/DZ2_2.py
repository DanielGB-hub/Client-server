# 2. Задание на закрепление знаний по модулю json.
# Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
# количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений
# каждого параметра.
import json
import datetime


def write_order_to_json(var_1, var_2, var_3, var_4, var_5):
    dict_to_json = {'item': var_1, 'quantity': var_2, 'price': var_3, 'buyer': var_4, 'date': str(var_5)}

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(dict_to_json, f_n, ensure_ascii=False, sort_keys=False, indent=4)
    print('\nСодержание файла orders.json:\n')
    with open('orders.json', encoding='utf-8') as f_n:
        print(f_n.read())


print("Пожалуйста, введите 5 параметров: наименование товара, количество, цена, покупатель, дата(dd.mm.yyyy): ")
print()
item = input("Введите наименование товара: ")

while True:
    try:
        quantity = int(input("Введите количество, шт: "))
        if quantity < 0:
            raise Exception
        break
    except ValueError:
        print('Неверный формат! Введите не отрицательное число!')
    except Exception:
        print('Количество не должно быть отрицательным!')

while True:
    try:
        price = int(input("Введите цену, руб: "))
        if price < 0:
            raise Exception
        break
    except ValueError:
        print('Неверный формат! Введите не отрицательное число!')
    except Exception:
        print('Цена не должна быть отрицательной!')
buyer = input("Введите имя покупателя, фио: ")

while True:
    date_ = input('Введите дату заказа (дд-мм-гггг): ')
    day, month, year = map(int, date_.split('-'))
    try:
        date = datetime.date(year, month, day)
        break
    except ValueError:
        print('Неверный формат даты!')


write_order_to_json(var_1=item, var_2=quantity, var_3=price, var_4=buyer, var_5=date)
