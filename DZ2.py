"""
Реализовать дескриптор для класса серверного сокета, а в нем — проверку номера порта. Это должно быть целое число (>=0).
 Значение порта по умолчанию равняется 7777. Дескриптор надо создать в отдельном классе.
 Его экземпляр добавить в пределах класса серверного сокета.
 Номер порта передается в экземпляр дескриптора при запуске сервера.

"""

#  Здесь расположен дескриптор порта для серверного сокета отдельным куском кода.
#  Такой же код встроен в код сервера сразу после импорта модулей. S_port.port применяется в 132 строке кода server.py


class BoundaryConditions:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 1024 or value > 65535:
            raise ValueError("Не может быть меньше 1024 и больше 65535")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class ServerPort:
    port = BoundaryConditions()

    def __init__(self, name, port):
        self._name = name
        self.port = port


S_port = ServerPort("port", 5555)
S_port.port = 1000  # тест работы дескриптора
