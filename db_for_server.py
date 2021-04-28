"""

Начать реализацию класса «Хранилище» для серверной стороны. Хранение необходимо
осуществлять в базе данных. В качестве СУБД использовать sqlite. Для взаимодействия с БД
можно применять ORM.
Опорная схема базы данных:
● На стороне сервера БД содержит следующие таблицы:

    ○ клиент:
        ■ логин;
        ■ информация.

    ○ история_клиента:
        ■ время входа;
        ■ ip-адрес.

    ○ список_контактов (составляется на основании выборки всех записей с
id_владельца):
        ■ id_владельца;
        ■ id_клиента.

"""

from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Numeric, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, exists, select

from sqlalchemy.orm import relationship

Base = declarative_base()


class Client(Base):  # таблица "Client" -> это класс Client(наследуется от декларативной базы Base)

    __tablename__ = "Client"  # название таблицы
    client_id = Column(Integer, primary_key=True)  # номер записи
    login = Column(String(20), unique=True)  # колонка с login (уникальное содержимое, длина 20 символов)
    password = Column(String(100))  # колонка с паролем (длина 100 символов)

    def __repr__(self):
        return f"<Client(id='{self.client_id}', login='{self.login}', password='{self.password}')>"


class ClientStorage:
    def __init__(self, session) -> None:
        self._session = session

    def add_client(self, login, password):
        try:
            with self._session.begin():
                self._session.add(Client(login=login, password=password))
        except IntegrityError as e:
            raise ValueError("Такой логин уже существует") from e

    def client_exists(self, login, password):
        stmt = exists().where(and_(Client.login == login, Client.password == password))
        return self._session.query(Client).filter(stmt).first() != None


class ClientHistory(Base):  # таблица "ClientHistory" -> это класс ClientHistory (наследуется от Base)
    __tablename__ = "ClientHistory"

    history_id = Column(Integer, primary_key=True)  # номер записи
    client_id = Column(Integer, ForeignKey("Client.client_id"))  # внешний ключ, как аргумент таблицы
    ip_address = Column(String(4 + 4 + 4 + 3))  # колонка для ip-адреса клиента
    when = Column(String)  # колонка для времени записи

    Client = relationship("Client", back_populates="ClientHistory")

    def __repr__(self):
        return f"<ClientHistory(id='{self.history_id}', client_id='{self.client_id}', ip_address='{self.ip_address}'," \
               f" when={self.when})>"


class ClientHistoryStorage:
    def __init__(self, session) -> None:
        self._session = session

    def add_record(self, client_id, ip_address, when):
        with self._session.begin():
            self._session.add(
                ClientHistory(client_id=client_id, ip_address=ip_address, when=when)
            )


class ContactList(Base):  # таблица "ContactList" -> это класс ContactList (наследуется от Base)
    __tablename__ = "ContactList"

    contact_id = Column(Integer, primary_key=True)  # номер записи
    #main_client_id = Column(Integer, ForeignKey("Client.client_id"))  # внешний ключ, как аргумент таблицы
    client_id = Column(Integer, ForeignKey("Client.client_id"))  # внешний ключ, как аргумент таблицы
    # Параметр back_populates указывается для реализации обратной связи из класса Client
    Client = relationship("Client", back_populates="ContactList")

    def __repr__(self):
        # При реализованных связях на уровне ORM
        return f"<ContactList(id='{self.contact_id}', client_id='{self.client_id}')>"


class ContactListStorage:
    def __init__(self, session) -> None:
        self._session = session

    def add_contact(self, client_id):
        with self._session.begin():
            self._session.add(
                ContactList(client_id=client_id)
            )


Client.ClientHistory = relationship("ClientHistory", order_by=ClientHistory.history_id, back_populates="Client")
Client.ContactList = relationship("ContactList", order_by=ContactList.contact_id, back_populates="Client")
